from pydantic import BaseModel

class RegisterForm(BaseModel):
    username: str
    password: str
    confirm_password: str

class LoginForm(BaseModel):
    username: str
    password: str

class SubscriptionForm(BaseModel):
    plan: str
    payment_method: str  # 'btc' or 'paypal'
    payment_details: str

class PaymentForm(BaseModel):
    method: str
    details: str
