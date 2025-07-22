
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)
db = client["LMBD"]  # Change to your database name

# Example collection
users_col = db["users"]
users_col = db["users"]
subs_col = db["subscriptions"]
payments_col = db["payments"]

