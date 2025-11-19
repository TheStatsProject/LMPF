from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse, Response
from fastapi.templating import Jinja2Templates
from markupsafe import Markup
import os
from docutils.core import publish_parts
from app.database import subs_col, users_col

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

def find_rst_file_for_slug(slug: str) -> str:
    """
    Given a slug like 'My-art' or 'my-art' return the absolute path to an .rst file in docs/source
    Tries a few common name variants.
    """
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs", "source"))
    candidates = [
        f"{slug}.rst",
        f"{slug.lower()}.rst",
        f"{slug.capitalize()}.rst",
        f"{slug.replace('-', '_')}.rst",
        f"{slug.replace('-', '').lower()}.rst"
    ]
    for fn in candidates:
        fp = os.path.join(base, fn)
        if os.path.isfile(fp):
            return fp
    # fallback: try exact list in directory (case-insensitive match)
    try:
        for fname in os.listdir(base):
            if fname.lower() == f"{slug.lower()}.rst":
                return os.path.join(base, fname)
    except Exception:
        pass
    return ""

def rst_to_html(rst_path: str) -> (str, str):
    """Convert an .rst file to HTML fragment (body) and title using docutils."""
    with open(rst_path, 'r', encoding='utf-8') as f:
        rst_src = f.read()
    parts = publish_parts(source=rst_src, writer_name='html5')
    html_body = parts.get('html_body', '')
    title = parts.get('title', '')
    return html_body, title

def user_is_subscribed(username: str) -> bool:
    if not username:
        return False
    sub = subs_col.find_one({"username": username})
    # also support subscription status on user document
    if sub and sub.get("payment_status") == "completed":
        return True
    u = users_col.find_one({"username": username})
    if u and u.get("payment_status") == "completed":
        return True
    return False

@router.get("/article/{slug}", response_class=HTMLResponse)
async def serve_article(request: Request, slug: str):
    """
    Serve an article located at docs/source/<slug>.rst (or similar).
    Enforce login and subscription:
      - If not logged in -> redirect to /login
      - If logged in but not subscribed -> redirect to /subscribe
      - If subscribed -> render the rst and display inside the article wrapper template
    Example: GET /article/My-art  will serve docs/source/My-art.rst
    """
    rst_path = find_rst_file_for_slug(slug)
    if not rst_path:
        return Response(status_code=404, content=f"Article '{slug}' not found.")

    username = request.session.get("user")
    if not username:
        # Not logged in, redirect to login page (can include next param if you want)
        return RedirectResponse("/login", status_code=302)

    if not user_is_subscribed(username):
        # Not subscribed -> send user to subscription page
        return RedirectResponse("/subscribe", status_code=302)

    # Render the .rst into HTML
    try:
        html_body, title = rst_to_html(rst_path)
    except Exception as e:
        return Response(status_code=500, content=f"Error rendering article: {e}")

    # Use a wrapper template that places the fragment into a standard site layout.
    content = Markup(html_body)
    return templates.TemplateResponse("article_page.html", {
        "request": request,
        "content": content,
        "title": title or slug,
        "slug": slug,
        "username": username
    })
