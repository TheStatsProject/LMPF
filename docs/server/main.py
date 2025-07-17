from fastapi import FastAPI, Request, Form, Depends, status
from fastapi.responses import RedirectResponse, HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from passlib.context import CryptContext
from pymongo import MongoClient
from starlette.middleware.sessions import SessionMiddleware
import os

# MongoDB config
MONGO_URL = "mongodb://localhost:27017"
client = MongoClient(MONGO_URL)
db = client["yourdbname"]
users_col = db["users"]

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# FastAPI setup
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")
templates = Jinja2Templates(directory="templates")

DOCS_DIR = os.path.abspath("../docs/_build/html")  # adjust path if needed

def get_user(username):
    return users_col.find_one({"username": username})

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def hash_password(password):
    return pwd_context.hash(password)

def is_authenticated(request: Request):
    return request.session.get("user")

@app.get("/register", response_class=HTMLResponse)
def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register")
def register(request: Request, username: str = Form(...), password: str = Form(...)):
    if get_user(username):
        return HTMLResponse("Username already taken.", status_code=400)
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
    if user and verify_password(password, user["password"]):
        request.session["user"] = username
        return RedirectResponse("/docs/", status_code=302)
    return HTMLResponse("Invalid credentials", status_code=401)

@app.get("/logout")
def logout(request: Request):
    request.session.pop("user", None)
    return RedirectResponse("/login", status_code=302)

# Serve docs only to authenticated users
@app.get("/docs/{path:path}", response_class=HTMLResponse)
def serve_docs(request: Request, path: str = ""):
    if not is_authenticated(request):
        return RedirectResponse("/login")
    file_path = os.path.join(DOCS_DIR, path or "index.html")
    if not os.path.isfile(file_path):
        return HTMLResponse("Not found", status_code=404)
    # serve as static file
    return FileResponse(file_path)

# Static assets (if Sphinx puts them in _static)
app.mount("/docs/_static", StaticFiles(directory=os.path.join(DOCS_DIR, "_static")), name="static")

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    if is_authenticated(request):
        return RedirectResponse("/docs/")
    return RedirectResponse("/login")
