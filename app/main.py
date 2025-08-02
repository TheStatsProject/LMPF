from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from fastapi.templating import Jinja2Templates
from app.config import SECRET_KEY
from app.routes import auth, subscription, payment
from app.database import db

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
app.include_router(auth.router)
app.include_router(subscription.router)
app.include_router(payment.router)
templates = Jinja2Templates(directory="app/templates")

@app.get("/ping")
async def ping():
    stats = await db.stats.find_one({})
    return stats or {"message": "Connected!"}
