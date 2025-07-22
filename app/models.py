# MongoDB helpers (can be expanded for 2FA, payments, etc.)
def get_user(username):
    from app.database import users_col
    return users_col.find_one({"username": username})

def create_user(username, password_hash):
    from app.database import users_col
    users_col.insert_one({"username": username, "password": password_hash})
    
def create_subscription(username, plan, payment_status):
    from app.database import subs_col
    subs_col.insert_one({
        "username": username,
        "plan": plan,
        "payment_status": payment_status
    })

def record_payment(username, method, details, status):
    from app.database import payments_col
    payments_col.insert_one({
        "username": username,
        "method": method,
        "details": details,
        "status": status
    })
