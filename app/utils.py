from passlib.context import CryptContext
import secrets

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def generate_2fa_code():
    return secrets.token_hex(3)  # 6-digit hex code

def verify_payment_btc(tx_hash):
    # Placeholder: integrate with a BTC API
    return True

def verify_payment_paypal(paypal_id):
    # Placeholder: integrate with PayPal API
    return True
