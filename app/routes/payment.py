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
