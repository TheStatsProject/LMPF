from pymongo import MongoClient
from app.config import MONGO_URL, DB_NAME

client = MongoClient(MONGO_URL)
db = client[DB_NAME]
users_col = db["users"]
subs_col = db["subscriptions"]
payments_col = db["payments"]
