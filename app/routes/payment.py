from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from app.models import record_payment
from app.utils import verify_payment_btc, verify_payment_paypal
from fastapi.templating import Jinja2Templates
import os

router = APIRouter()
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "../../docs/server/templates"))

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
    record_payment(username, method, details, status)
    return templates.TemplateResponse("profile.html", {"request": request, "username": username, "payment_status": status})
