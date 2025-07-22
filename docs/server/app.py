import os
import secrets
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from passlib.context import CryptContext
from pymongo import MongoClient, errors
from starlette.middleware.sessions import SessionMiddleware

MONGO_URL = os.environ.get(
    "MONGO_URL",
    "mongodb+srv://digroom:<db_password>@cluster0.i5s27i0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)
SECRET_KEY = os.environ.get("SESSION_SECRET_KEY") or secrets.token_urlsafe(32)
DB_NAME = os.environ.get("MONGO_DB_NAME", "lmpf_docs")

try:
    client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=5000)
    client.server_info()
except errors.ConnectionFailure:
    raise RuntimeError("Cannot connect to MongoDB. Check MONGO_URL and network.")

db = client[DB_NAME]
users_col = db["users"]
users_col.create_index("username", unique=True)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI()

STATIC_PATH = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")

TEMPLATES_PATH = os.path.join(os.path.dirname(__file__), "templates")
templates = Jinja2Templates(directory=TEMPLATES_PATH)

app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

def get_user(username: str):
    return users_col.find_one({"username": username})

def verify_password(plain: str, hashed: str):
    return pwd_context.verify(plain, hashed)

def hash_password(password: str):
    return pwd_context.hash(password)

def get_authenticated_username(request: Request):
    return request.session.get("user")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    user = get_authenticated_username(request)
    return templates.TemplateResponse("home.html", {"request": request, "user": user})

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
        "password": hash_password(password)
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

@app.get("/profile", response_class=HTMLResponse)
def profile(request: Request):
    username = get_authenticated_username(request)
    if not username:
        return RedirectResponse("/login", status_code=302)
    return templates.TemplateResponse("profile.html", {"request": request, "username": username})
