from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from app.database import users_col, subs_col
from app.utils import hash_password, verify_password

app = FastAPI(
    title="Labor Market & Population Forecaster",
    description="API Toolkit for Labor Market and Population Forecasting.",
    version="0.1.0"
)

templates = Jinja2Templates(directory="app/templates")

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

@app.get("/register", response_class=HTMLResponse, include_in_schema=False)
async def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request, "error": None})

@app.post("/register", response_class=HTMLResponse, include_in_schema=False)
async def register_submit(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...)
):
    error = None
    if users_col.find_one({"username": username}):
        error = "Username already exists. Please choose another."
    elif len(password) < 8:
        error = "Password must be at least 8 characters."
    elif password != confirm_password:
        error = "Passwords do not match."
    if error:
        return templates.TemplateResponse("register.html", {"request": request, "error": error})
    hashed_pw = hash_password(password)
    users_col.insert_one({"username": username, "password": hashed_pw})
    return RedirectResponse("/login", status_code=302)

@app.get("/login", response_class=HTMLResponse, include_in_schema=False)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "error": None})

@app.post("/login", response_class=HTMLResponse, include_in_schema=False)
async def login_submit(request: Request, username: str = Form(...), password: str = Form(...)):
    user = users_col.find_one({"username": username})
    error = None
    if not user:
        error = "User not found."
    elif not verify_password(password, user["password"]):
        error = "Invalid password."
    if error:
        return templates.TemplateResponse("login.html", {"request": request, "error": error})
    # Could set session here if you add session middleware later
    return templates.TemplateResponse("profile.html", {"request": request, "username": username, "payment_status": user.get("payment_status")})

@app.get("/subscribe", response_class=HTMLResponse, include_in_schema=False)
async def subscribe_form(request: Request):
    return templates.TemplateResponse("subscribe.html", {"request": request})

@app.post("/subscribe", response_class=HTMLResponse, include_in_schema=False)
async def subscribe_submit(
    request: Request,
    plan: str = Form(...),
    payment_method: str = Form(...),
    payment_details: str = Form(...)
):
    # You could check for duplicate subscriptions if you wish
    subs_col.insert_one({
        "plan": plan,
        "payment_method": payment_method,
        "payment_details": payment_details
    })
    return templates.TemplateResponse("payment.html", {"request": request})

# Add other routes (profile, payment, etc.) as needed!

from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from app.config import SECRET_KEY
from app.routes import auth, subscription, payment
# new articles router
from app.routes.articles import router as articles_router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI(
    title="Labor Market & Population Forecaster",
    description="API Toolkit for Labor Market and Population Forecasting.",
    version="0.1.0"
)

# Session middleware (SESSION_SECRET_KEY must be set in .env)
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

# Include routers
app.include_router(auth.router, prefix="")
app.include_router(subscription.router, prefix="")
app.include_router(payment.router, prefix="")
app.include_router(articles_router, prefix="")

templates = Jinja2Templates(directory="app/templates")

@app.get("/", include_in_schema=False)
async def root():
    # Provide a lightweight index / link to docs or articles
    return RedirectResponse(url="/docs")

# Keep existing register/login/register routes defined in auth/main; if you used previous
# main handlers remove duplicates to avoid conflicts.
