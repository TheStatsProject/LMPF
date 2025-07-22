from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from app.models import get_user, create_user
from app.utils import hash_password, verify_password
from fastapi.templating import Jinja2Templates
import os

router = APIRouter()
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "../../docs/server/templates"))

@router.get("/login", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    user = get_user(username)
    if not user or not verify_password(password, user["password"]):
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials."})
    request.session["user"] = username
    return RedirectResponse("/profile", status_code=302)

@router.get("/register", response_class=HTMLResponse)
def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.post("/register")
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
    create_user(username, hash_password(password))
    return RedirectResponse("/login", status_code=302)

@router.get("/profile", response_class=HTMLResponse)
def profile(request: Request):
    username = request.session.get("user")
    if not username:
        return RedirectResponse("/login", status_code=302)
    return templates.TemplateResponse("profile.html", {"request": request, "username": username})

@router.get("/2fa", response_class=HTMLResponse)
def twofa_form(request: Request):
    return templates.TemplateResponse("2fa.html", {"request": request})

@router.post("/2fa")
def twofa_verify(request: Request, code: str = Form(...)):
    user = get_user(request.session["user"])
    if user and user["2fa_enabled"]:
        if verify_totp(user["2fa_secret"], code):
            request.session["2fa_verified"] = True
            return RedirectResponse("/profile", status_code=302)
        return templates.TemplateResponse("2fa.html", {"request": request, "error": "Invalid 2FA code."})
    return RedirectResponse("/login", status_code=302)
    
