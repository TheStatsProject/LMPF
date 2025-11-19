from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from app.models import create_subscription, record_payment
from app.utils import verify_payment_btc, verify_payment_paypal
from fastapi.templating import Jinja2Templates
import os
from app.database import subs_col, payments_col, users_col

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.post("/payment")
def payment(request: Request, method: str = Form(...), details: str = Form(...)):
    username = request.session.get("user")
    if not username:
        return RedirectResponse("/login", status_code=302)

    status = "failed"
    if method == "btc" and verify_payment_btc(details):
        status = "completed"
    elif method == "paypal" and verify_payment_paypal(details):
        status = "completed"

    # Record a payment audit
    record_payment(username, method, details, status)

    # Update subscription state: if there's a pending subscription record, mark it completed.
    subs_col.update_one({"username": username, "payment_status": {"$in": ["pending", None]}},
                        {"$set": {"payment_status": status}}, upsert=False)

    # Also reflect on user document for convenience
    if status == "completed":
        users_col.update_one({"username": username}, {"$set": {"payment_status": "completed"}})

    return templates.TemplateResponse("payment.html", {"request": request, "username": username, "payment_status": status})
