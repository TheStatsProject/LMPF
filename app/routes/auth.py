from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from app.models import get_user, create_user
from app.utils import hash_password, verify_password, generate_totp_secret, verify_totp
from fastapi.templating import Jinja2Templates
import os

router = APIRouter()
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "../../docs/server/templates"))

# GET login page
@router.get("/login", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "error": None})

# POST login (with async MongoDB)
@router.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    user = await get_user(username)
    error = None
    if not user:
        error = "User not found."
    elif not verify_password(password, user["password"]):
        error = "Invalid password."
    if error:
        return templates.TemplateResponse("login.html", {"request": request, "error": error})
    request.session["user"] = username
    # If 2FA is enabled, redirect to 2FA
    if user.get("2fa_enabled"):
        return RedirectResponse("/2fa", status_code=302)
    return RedirectResponse("/profile", status_code=302)

# GET register page
@router.get("/register", response_class=HTMLResponse)
async def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request, "error": None})

# POST register (with async MongoDB and 2FA setup)
@router.post("/register")
async def register(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...)
):
    error = None
    username_error = password_error = confirm_error = None
    existing = await get_user(username)
    if existing:
        username_error = "Username already taken."
        error = username_error
    elif len(password) < 8:
        password_error = "Password must be at least 8 characters."
        error = password_error
    elif password != confirm_password:
        confirm_error = "Passwords do not match."
        error = confirm_error
    if error:
        return templates.TemplateResponse(
            "register.html",
            {
                "request": request,
                "error": error,
                "username_error": username_error,
                "password_error": password_error,
                "confirm_error": confirm_error,
            }
        )
    totp_secret = generate_totp_secret()
    await create_user(username, hash_password(password), totp_secret=totp_secret)
    # Optionally, show QR code or secret for user to set up 2FA app
    return RedirectResponse("/login", status_code=302)

# GET profile
@router.get("/profile", response_class=HTMLResponse)
async def profile(request: Request):
    username = request.session.get("user")
    if not username:
        return RedirectResponse("/login", status_code=302)
    user = await get_user(username)
    payment_status = user.get("payment_status") if user else None
    return templates.TemplateResponse("profile.html", {"request": request, "username": username, "payment_status": payment_status})

# GET 2FA page
@router.get("/2fa", response_class=HTMLResponse)
async def twofa_form(request: Request):
    return templates.TemplateResponse("2fa.html", {"request": request, "error": None})

# POST 2FA verify
@router.post("/2fa")
async def twofa_verify(request: Request, code: str = Form(...)):
    username = request.session.get("user")
    if not username:
        return RedirectResponse("/login", status_code=302)
    user = await get_user(username)
    if user and user.get("2fa_enabled"):
        if verify_totp(user["2fa_secret"], code):
            request.session["2fa_verified"] = True
            return RedirectResponse("/profile", status_code=302)
        return templates.TemplateResponse("2fa.html", {"request": request, "error": "Invalid 2FA code."})
    return RedirectResponse("/login", status_code=302)

# GET logout
@router.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/login", status_code=302)

# GET reset password page
@router.get("/reset", response_class=HTMLResponse)
async def reset_form(request: Request):
    return templates.TemplateResponse("reset.html", {"request": request, "error": None})

# POST reset password
@router.post("/reset")
async def reset_password(
    request: Request,
    email: str = Form(...),
    code: str = Form(...),
    new_password: str = Form(...)
):
    # TODO: Implement email code verification and password update
    return templates.TemplateResponse("reset.html", {"request": request, "error": "Feature not yet implemented."})
