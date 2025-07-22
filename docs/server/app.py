import os
import secrets
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from passlib.context import CryptContext
from pymongo import MongoClient
from starlette.middleware.sessions import SessionMiddleware



app = FastAPI()

# Connect to MongoDB (replace with your credentials/connection string)
MONGO_URL = "mongodb+srv://digroom:<db_password>@cluster0.i5s27i0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URL)
db = client["mydb"]  # Use your database name
collection = db["mycollection"]  # Use your collection name

@app.get("/items")
def get_items():
    # Get all documents in the collection
    items = list(collection.find({}, {"_id": 0}))  # Exclude MongoDB's _id field
    return items


# --- Config ---
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://digroom:<db_password>@cluster0.i5s27i0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
SECRET_KEY = os.environ.get("SESSION_SECRET_KEY") or secrets.token_urlsafe(32)
DB_NAME = os.environ.get("MONGO_DB_NAME", "lmpf_docs")

client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=5000)
db = client[DB_NAME]
users_col = db["users"]
users_col.create_index("username", unique=True)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

# Mount static files
STATIC_PATH = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")

TEMPLATES_PATH = os.path.join(os.path.dirname(__file__), "templates")
templates = Jinja2Templates(directory=TEMPLATES_PATH)

# --- Utilities ---
def get_user(username: str):
    return users_col.find_one({"username": username})

def verify_password(plain: str, hashed: str):
    return pwd_context.verify(plain, hashed)

def hash_password(password: str):
    return pwd_context.hash(password)

def get_authenticated_username(request: Request):
    return request.session.get("user")

# --- Routes ---
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

@app.get("/profile", response_class=HTMLResponse)
def profile(request: Request):
    username = get_authenticated_username(request)
    if not username:
        return RedirectResponse("/login", status_code=302)
    return templates.TemplateResponse("profile.html", {"request": request, "username": username})

@app.get("/logout")
def logout(request: Request):
    request.session.pop("user", None)
    return RedirectResponse("/login", status_code=302)
