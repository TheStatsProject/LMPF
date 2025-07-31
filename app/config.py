from dotenv import load_dotenv
import os

# Automatically load .env file at startup
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "lmpf_db")

# Config values with defaults and error handling
SECRET_KEY = os.environ.get("SESSION_SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SESSION_SECRET_KEY not set in environment variables.")

MONGO_URL = os.environ.get("MONGO_URL")
if not MONGO_URL:
    raise ValueError("MONGO_URL not set in environment variables.")

DB_NAME = os.environ.get("MONGO_DB_NAME", "lmpf_docs")

EMAIL_API_KEY = os.environ.get("EMAIL_API_KEY", "")
SMS_API_KEY = os.environ.get("SMS_API_KEY", "")

# Additional config options for extensibility
PAYPAL_CLIENT_ID = os.environ.get("PAYPAL_CLIENT_ID", "")
PAYPAL_SECRET = os.environ.get("PAYPAL_SECRET", "")
BTC_API_KEY = os.environ.get("BTC_API_KEY", "")

# Example: Use this config in other modules
# from app.config import SECRET_KEY, MONGO_URL, DB_NAME, EMAIL_API_KEY, SMS_API_KEY, PAYPAL_CLIENT_ID, PAYPAL_SECRET, BTC_API_KEY
