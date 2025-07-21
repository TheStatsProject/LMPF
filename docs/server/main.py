import os
import secrets
from fastapi import FastAPI, Request, Form, status
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from passlib.context import CryptContext
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from starlette.middleware.sessions import SessionMiddleware

from authlib.integrations.starlette_client import OAuth

# --- Configuration ---

mongodb+srv://digroom:<db_password>@cluster0.i5s27i0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
SECRET_KEY = os.environ.get("SESSION_SECRET_KEY") or secrets.token_urlsafe(32)
DB_NAME = os.environ.get("MONGO_DB_NAME", "lmpf_docs")

# --- MongoDB Connection ---

client = MongoClient(MONGO_URL)
db = client[DB_NAME]
users_col = db["users"]
users_col.create_index("username", unique=True)

# --- Password Hashing ---

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# --- FastAPI App ---

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))

# --- OAuth Setup ---

oauth = OAuth()
oauth.register(
    name='github',
    client_id=os.environ.get('GITHUB_CLIENT_ID', 'your_github_client_id'),
    client_secret=os.environ.get('GITHUB_CLIENT_SECRET', 'your_github_client_secret'),
    access_token_url='https://github.com/login/oauth/access_token',
    access_token_params=None,
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params=None,
    api_base_url='https://api.github.com/',
    userinfo_endpoint='https://api.github.com/user',
    client_kwargs={'scope': 'user:email'},
)

# --- Utilities ---

def get_user(username: str):
    return users_col.find_one({"username": username})

def verify_password(plain: str, hashed: str):
    return pwd_context.verify(plain, hashed)

def hash_password(password: str):
    return pwd_context.hash(password)

def is_authenticated(request: Request):
    return bool(request.session.get("user"))

def get_authenticated_username(request: Request):
    return request.session.get("user")

# --- Routes ---

@app.get("/register", response_class=HTMLResponse)
def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register")
def register(request: Request, username: str = Form(...), password: str = Form(...), confirm_password: str = Form(...)):
    error = None
    if get_user(username):
        error = "Username already taken."
    elif len(password) < 8:
        error = "Password must be at least 8 characters."
    elif password != confirm_password:
        error = "Passwords do not match."
    if error:
        return templates.TemplateResponse("register.html", {"request": request, "error": error})
    users_col.insert_one({
        "username": username,
        "password": hash_password(password),
        "auth_type": "local"
    })
    return RedirectResponse("/login", status_code=302)

@app.get("/login", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    user = get_user(username)
    if not user or not verify_password(password, user["password"]):
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials."})
    request.session["user"] = username
    return RedirectResponse("/", status_code=302)

@app.get("/logout")
def logout(request: Request):
    request.session.pop("user", None)
    return RedirectResponse("/login", status_code=302)

# --- GitHub OAuth routes ---

@app.get("/login/github")
async def login_github(request: Request):
    redirect_uri = request.url_for('auth_github')
    return await oauth.github.authorize_redirect(request, redirect_uri)

@app.get("/auth/github")
async def auth_github(request: Request):
    token = await oauth.github.authorize_access_token(request)
    user_data = await oauth.github.parse_id_token(request, token)
    github_user = await oauth.github.get('user', token=token)
    profile = github_user.json()
    username = profile["login"]
    user = get_user(username)
    if not user:
        users_col.insert_one({
            "username": username,
            "auth_type": "github",
            "github_id": profile["id"],
            "email": profile.get("email", "")
        })
    request.session["user"] = username
    return RedirectResponse("/", status_code=302)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    user = get_authenticated_username(request)
    return templates.TemplateResponse("home.html", {"request": request, "user": user})
