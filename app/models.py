# MongoDB helpers (Motor async)
from app.database import db

async def get_user(username):
    return await db.users.find_one({"username": username})

async def create_user(username, password_hash, totp_secret=None):
    user_doc = {
        "username": username,
        "password": password_hash,
        "2fa_enabled": bool(totp_secret),
        "2fa_secret": totp_secret,
        "payment_status": None
    }
    return await db.users.insert_one(user_doc)

async def create_subscription(username, plan, payment_status):
    sub_doc = {
        "username": username,
        "plan": plan,
        "payment_status": payment_status
    }
    return await db.subscriptions.insert_one(sub_doc)

async def record_payment(username, method, details, status):
    payment_doc = {
        "username": username,
        "method": method,
        "details": details,
        "status": status
    }
    return await db.payments.insert_one(payment_doc)
