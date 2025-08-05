from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.config import SECRET_KEY
from app.routes import auth, subscription, payment
from app.database import db

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
app.include_router(auth.router, prefix="/api/auth")
app.include_router(subscription.router, prefix="/api/subscription")
app.include_router(payment.router, prefix="/api/payment")

# Serve built docs (index.html generated from index.rst) at root
app.mount("/", StaticFiles(directory="docs", html=True), name="docs")

# Templates for server-side rendering, if needed
templates = Jinja2Templates(directory="app/templates")

@app.get("/ping")
async def ping():
    stats = await db.stats.find_one({})
    return stats or {"message": "Connected!"}
