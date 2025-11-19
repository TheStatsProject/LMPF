from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles
import os

from app.config import SECRET_KEY
from app.routes import auth, subscription, payment
from app.routes.articles import router as articles_router

# Create app
app = FastAPI(
    title="Labor Market & Population Forecaster",
    description="API Toolkit for Labor Market and Population Forecasting.",
    version="0.1.0",
)

# Session middleware — make sure SESSION_SECRET_KEY is set in .env
# Configure secure options (https_only True recommended in production)
app.add_middleware(
    SessionMiddleware,
    secret_key=SECRET_KEY,
    session_cookie="lmpf_session",
    max_age=60 * 60 * 24 * 30,  # 30 days
    https_only=False,  # set to True in production
    same_site="lax",
)

# Mount static folders (templates will reference files under /static if needed)
# Ensure these directories exist in your repo: app/static and docs/build/html (if you pre-build Sphinx)
app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "static")), name="static")

# Optional: if you build Sphinx locally and want to serve pre-built HTML
# mount the built docs directory at /prebuilt-docs (do not expose in production without careful checks)
prebuilt_docs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs", "build", "html"))
if os.path.isdir(prebuilt_docs_path):
    app.mount("/prebuilt-docs", StaticFiles(directory=prebuilt_docs_path), name="prebuilt-docs")

# Register routers (auth must be included so login/register routes use sessions)
app.include_router(auth.router, prefix="")
app.include_router(subscription.router, prefix="")
app.include_router(payment.router, prefix="")
app.include_router(articles_router, prefix="")

# Templates
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))

@app.get("/", include_in_schema=False)
async def root():
    """
    Root landing: redirect to RTD-style docs (/docs) or to a lightweight index.
    Change to a custom index if you prefer.
    """
    return RedirectResponse(url="/docs")

# Small convenience route: serve a pre-built Sphinx article behind the same session+subscription checks.
# This is optional; you can rely on the articles router that converts .rst -> HTML on the fly.
from app.database import users_col, subs_col
from fastapi import Depends
from typing import Optional
from fastapi.responses import Response

def _user_from_session(request: Request) -> Optional[str]:
    return request.session.get("user")

def _user_is_subscribed(username: Optional[str]) -> bool:
    if not username:
        return False
    sub = subs_col.find_one({"username": username})
    if sub and sub.get("payment_status") == "completed":
        return True
    u = users_col.find_one({"username": username})
    if u and u.get("payment_status") == "completed":
        return True
    return False

@app.get("/prebuilt-article/{slug}", response_class=Response, include_in_schema=False)
async def prebuilt_article(request: Request, slug: str):
    """
    Serve docs/build/html/en/latest/<slug>.html behind login & subscription.
    Useful if your .rst depend on Sphinx processing / extensions.
    """
    username = _user_from_session(request)
    if not username:
        return RedirectResponse("/login", status_code=302)
    if not _user_is_subscribed(username):
        return RedirectResponse("/subscribe", status_code=302)

    # Map slug to filename variants and check existence
    candidates = [
        f"{slug}.html",
        f"{slug.lower()}.html",
        f"{slug.replace('-', '_')}.html",
        f"{slug.replace('-', '')}.html",
    ]
    base = os.path.join(prebuilt_docs_path, "en", "latest") if os.path.isdir(os.path.join(prebuilt_docs_path, "en", "latest")) else prebuilt_docs_path
    for candidate in candidates:
        path = os.path.join(base, candidate)
        if os.path.isfile(path):
            return FileResponse(path, media_type="text/html")

    return Response(status_code=404, content=f"Prebuilt article '{slug}' not found.")
