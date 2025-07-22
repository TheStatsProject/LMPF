from passlib.context import CryptContext
import secrets
import pyotp

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

def generate_totp_secret():
    return pyotp.random_base32()

def get_totp(secret):
    return pyotp.TOTP(secret)

def verify_totp(secret, code):
    return pyotp.TOTP(secret).verify(code)

def verify_payment_btc(tx_hash):
    # Placeholder, integrate with BTC API/block explorer later
    return True

def verify_payment_paypal(paypal_id):
    # Placeholder for PayPal verification
    return True
