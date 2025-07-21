import os
import secrets
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from passlib.context import CryptContext
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from starlette.middleware.sessions import SessionMiddleware

# --- Configuration ---

MONGO_URL = os.environ.get(
    "MONGO_URL",
    "mongodb+srv://digroom:<db_password>@cluster0.i5s27i0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)
if not MONGO_URL:
    raise RuntimeError("MONGO_URL environment variable must be set for secure operation.")

SECRET_KEY = os.environ.get(
    "SESSION_SECRET_KEY",
    secrets.token_urlsafe(64)  # Automatically generate a secure key if not provided
)
DB_NAME = os.environ.get("MONGO_DB_NAME", "lmpf_docs")

DOCS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../build/html"))

# --- MongoDB Connection ---
try:
    client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=5000)
    client.server_info()
except ConnectionFailure as e:
    raise RuntimeError(f"Cannot connect to MongoDB: {e}")

db = client[DB_NAME]
users_col = db["users"]

# --- Password Hashing ---
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# --- FastAPI App ---
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))

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
def register(request: Request, username: str = Form(...), password: str = Form(...)):
    if get_user(username):
        return HTMLResponse("Username already taken.", status_code=400)
    if len(password) < 8:
        return HTMLResponse("Password must be at least 8 characters.", status_code=400)
    # For 2FA: generate a user-specific secret (e.g., pyotp.random_base32()) and store it here
    users_col.insert_one({
        "username": username,
        "password": hash_password(password),
        # "2fa_secret": pyotp.random_base32()  # Uncomment if adding 2FA
    })
    return RedirectResponse("/login", status_code=302)

@app.get("/login", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    user = get_user(username)
    if not user or not verify_password(password, user["password"]):
        return HTMLResponse("Invalid credentials.", status_code=401)
    # For 2FA: Here you would require a second step before logging in, e.g. send a code or ask for TOTP
    request.session["user"] = username
    return RedirectResponse("/docs/", status_code=302)

@app.get("/logout")
def logout(request: Request):
    request.session.pop("user", None)
    return RedirectResponse("/login", status_code=302)

@app.get("/profile", response_class=HTMLResponse)
def profile(request: Request):
    user = get_authenticated_username(request)
    if not user:
        return RedirectResponse("/login")
    return templates.TemplateResponse("profile.html", {"request": request, "username": user})

@app.get("/docs/{path:path}", response_class=HTMLResponse)
def serve_docs(request: Request, path: str = ""):
    if not is_authenticated(request):
        return RedirectResponse("/login")
    file_path = os.path.join(DOCS_DIR, path or "index.html")
    if not os.path.isfile(file_path):
        return HTMLResponse("Not found", status_code=404)
    return FileResponse(file_path)

# Serve Sphinx static assets
app.mount("/docs/_static", StaticFiles(directory=os.path.join(DOCS_DIR, "_static")), name="static")

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    if is_authenticated(request):
        return RedirectResponse("/docs/")
    return RedirectResponse("/login")

@app.get("/health")
def health():
    try:
        client.admin.command("ping")
        return JSONResponse({"status": "ok"})
    except Exception as e:
        return JSONResponse({"status": "error", "detail": str(e)}, status_code=503)
