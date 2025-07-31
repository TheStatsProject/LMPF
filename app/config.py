import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB configuration
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
MONGO_URL = os.getenv("MONGO_URL", MONGODB_URI)
DB_NAME = os.getenv("MONGO_DB_NAME", "LMBD")  # Default and aligns with database.py

# Application secret key (required)
SECRET_KEY = os.getenv("SESSION_SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SESSION_SECRET_KEY not set in environment variables or .env file.")

# Email and SMS API keys (optional, but log if missing)
EMAIL_API_KEY = os.getenv("EMAIL_API_KEY")
SMS_API_KEY = os.getenv("SMS_API_KEY")

if not EMAIL_API_KEY:
    print("[config.py] Warning: EMAIL_API_KEY not set.")
if not SMS_API_KEY:
    print("[config.py] Warning: SMS_API_KEY not set.")

# Payment and crypto API keys (optional)
PAYPAL_CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID")
PAYPAL_SECRET = os.getenv("PAYPAL_SECRET")
BTC_API_KEY = os.getenv("BTC_API_KEY")

# Example usage comment
# from app.config import SECRET_KEY, MONGO_URL, DB_NAME, EMAIL_API_KEY, SMS_API_KEY, PAYPAL_CLIENT_ID, PAYPAL_SECRET, BTC_API_KEY

# Optionally: Add a function to get MongoDB client, for easy importing
def get_mongo_client():
    from pymongo import MongoClient
    return MongoClient(MONGO_URL)
