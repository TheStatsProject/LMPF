from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from app.models import get_user, create_subscription
from app.database import subs_col, users_col

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

def user_is_subscribed(username: str) -> bool:
    if not username:
        return False
    sub = subs_col.find_one({"username": username})
    return bool(sub and sub.get("payment_status") == "completed")

@router.get("/article/my-art", response_class=HTMLResponse)
async def my_art(request: Request):
    username = request.session.get("user")
    if not username:
        # not logged in -> send to login page (or show subscription/signup page)
        return RedirectResponse("/login", status_code=302)
    if not user_is_subscribed(username):
        # send to subscription page
        return RedirectResponse("/subscribe", status_code=302)
    # Render the article template — copy the My-art content into app/templates/my_art.html
    return templates.TemplateResponse("my_art.html", {"request": request, "username": username})
