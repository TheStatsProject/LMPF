from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import pymongo
import os

app = FastAPI(
    title="The Truth Project",
    description="Labor Market and Population Forecasting Toolkit",
    version="0.1.0"
)

# MongoDB connection (set MONGODB_URI in Railway variables)
client = pymongo.MongoClient(os.environ.get("MONGODB_URI"))
db = client["yourdbname"]  # Change to your actual db name

@app.get("/", include_in_schema=False)
async def root():
    """Redirects root to the docs index."""
    return RedirectResponse(url="/docs/source/index.rst")

@app.get("/api/items")
async def api_items():
    """API endpoint for items in the MongoDB collection (returns JSON)."""
    items = list(db["yourcollection"].find())  # Change to your actual collection
    # Convert ObjectId to string for JSON serializability
    for item in items:
        item["_id"] = str(item["_id"])
    return {"items": items}
