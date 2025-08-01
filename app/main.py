from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from app.config import SECRET_KEY
from app.routes import auth, subscription, payment

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

app.include_router(auth.router)
app.include_router(subscription.router)
app.include_router(payment.router)

# Add this for template rendering:
templates = Jinja2Templates(directory="app/templates")

from fastapi import FastAPI
from .database import db


@app.get("/ping")
async def ping():
    stats = await db.stats.find_one({})
    return stats or {"message": "Connected!"}
