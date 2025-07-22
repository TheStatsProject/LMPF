from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from app.models import create_subscription
from fastapi.templating import Jinja2Templates
import os

router = APIRouter()
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "../../docs/server/templates"))

@router.get("/subscribe", response_class=HTMLResponse)
def subscribe_form(request: Request):
    return templates.TemplateResponse("subscribe.html", {"request": request})

@router.post("/subscribe")
def subscribe(request: Request, plan: str = Form(...), payment_method: str = Form(...), payment_details: str = Form(...)):
    username = request.session.get("user")
    if not username:
        return RedirectResponse("/login", status_code=302)
    create_subscription(username, plan, "pending")
    # Render payment page after subscription
    return templates.TemplateResponse("payment.html", {
        "request": request,
        "plan": plan,
        "payment_method": payment_method,
        "payment_details": payment_details
    })
