from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from app.database import users_col, subs_col  # Import from your central config

app = FastAPI(
    title="Labor Market & Population Forecaster",
    description="API Toolkit for Labor Market and Population Forecasting. Provides endpoints for data queries and predictive insights.",
    version="0.1.0"
)

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

@app.get("/register", response_class=HTMLResponse, include_in_schema=False)
async def register_form():
    return """
    <h1>Register</h1>
    <form method="post">
      Username: <input name="username"><br>
      Email: <input name="email"><br>
      Password: <input name="password" type="password"><br>
      <button type="submit">Register</button>
    </form>
    """

@app.post("/register", response_class=HTMLResponse, include_in_schema=False)
async def register_submit(username: str = Form(...), email: str = Form(...), password: str = Form(...)):
    users_col.insert_one({"username": username, "email": email, "password": password})
    return f"<h2>Welcome, {username}! Registration successful.</h2>"

@app.get("/login", response_class=HTMLResponse, include_in_schema=False)
async def login_form():
    return """
    <h1>Login</h1>
    <form method="post">
      Username: <input name="username"><br>
      Password: <input name="password" type="password"><br>
      <button type="submit">Login</button>
    </form>
    """

@app.post("/login", response_class=HTMLResponse, include_in_schema=False)
async def login_submit(username: str = Form(...), password: str = Form(...)):
    user = users_col.find_one({"username": username, "password": password})
    if user:
        return f"<h2>Welcome back, {username}!</h2>"
    return "<h2>Login failed. Please try again.</h2>"

@app.get("/subscribe", response_class=HTMLResponse, include_in_schema=False)
async def subscribe_form():
    return """
    <h1>Subscribe</h1>
    <form method="post">
      Email: <input name="email"><br>
      Plan: <select name="plan">
        <option value="basic">Basic</option>
        <option value="premium">Premium</option>
      </select><br>
      <button type="submit">Subscribe</button>
    </form>
    """

@app.post("/subscribe", response_class=HTMLResponse, include_in_schema=False)
async def subscribe_submit(email: str = Form(...), plan: str = Form(...)):
    subs_col.insert_one({"email": email, "plan": plan})
    return f"<h2>Subscription successful for {email} on the {plan} plan.</h2>"
