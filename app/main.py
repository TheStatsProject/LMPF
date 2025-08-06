from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import pymongo
import os

app = FastAPI(
    title="Labor Market & Population Forecaster",
    description="API Toolkit for Labor Market and Population Forecasting. Provides endpoints for data queries and predictive insights.",
    version="0.1.0"
)

# MongoDB connection (set MONGODB_URI in Railway variables)
client = pymongo.MongoClient(os.environ.get("MONGODB_URI"))
db = client["LMBD"]  # Change to your actual db name

@app.get("/", include_in_schema=False)
async def root():
    """Redirects root to the docs index."""
    return RedirectResponse(url="/docs/source/index.rst")

@app.get("/api/market-items")
async def get_market_items():
    """Returns labor market items from the MongoDB collection."""
    items = list(db["yourcollection"].find())  # Change to your actual collection
    for item in items:
        item["_id"] = str(item["_id"])
    return {"items": items}

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs/source/index.rst")

@app.get("/register", response_class=HTMLResponse, include_in_schema=False)
async def register():
    return "<h1>Register Page (TODO: Implement registration form)</h1>"

@app.get("/login", response_class=HTMLResponse, include_in_schema=False)
async def login():
    return "<h1>Login Page (TODO: Implement login form)</h1>"

@app.get("/subscribe", response_class=HTMLResponse, include_in_schema=False)
async def subscribe():
    return "<h1>Subscribe Page (TODO: Implement subscription form)</h1>"
