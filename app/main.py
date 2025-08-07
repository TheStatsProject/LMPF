from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from app.database import users_col, subs_col  # Import from your central config
from app.utils import hash_password, verify_password  # Secure password handling

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
      Username: <input name="username" required><br>
      Email: <input name="email" required><br>
      Password: <input name="password" type="password" required><br>
      <button type="submit">Register</button>
    </form>
    """

@app.post("/register", response_class=HTMLResponse, include_in_schema=False)
async def register_submit(username: str = Form(...), email: str = Form(...), password: str = Form(...)):
    # Check for duplicate username/email
    if users_col.find_one({"username": username}):
        return "<h2>Username already exists. Please choose another.</h2>"
    if users_col.find_one({"email": email}):
        return "<h2>Email already in use. Please use another email.</h2>"
    # Hash the password before storing
    hashed_pw = hash_password(password)
    users_col.insert_one({"username": username, "email": email, "password": hashed_pw})
    return f"<h2>Welcome, {username}! Registration successful.</h2>"

@app.get("/login", response_class=HTMLResponse, include_in_schema=False)
async def login_form():
    return """
    <h1>Login</h1>
    <form method="post">
      Username: <input name="username" required><br>
      Password: <input name="password" type="password" required><br>
      <button type="submit">Login</button>
    </form>
    """

@app.post("/login", response_class=HTMLResponse, include_in_schema=False)
async def login_submit(username: str = Form(...), password: str = Form(...)):
    user = users_col.find_one({"username": username})
    if user and verify_password(password, user["password"]):
        return f"<h2>Welcome back, {username}!</h2>"
    return "<h2>Login failed. Please check your credentials and try again.</h2>"

@app.get("/subscribe", response_class=HTMLResponse, include_in_schema=False)
async def subscribe_form():
    return """
    <h1>Subscribe</h1>
    <form method="post">
      Email: <input name="email" required><br>
      Plan: <select name="plan" required>
        <option value="basic">Basic</option>
        <option value="premium">Premium</option>
      </select><br>
      <button type="submit">Subscribe</button>
    </form>
    """

@app.post("/subscribe", response_class=HTMLResponse, include_in_schema=False)
async def subscribe_submit(email: str = Form(...), plan: str = Form(...)):
    # Optionally check if already subscribed
    if subs_col.find_one({"email": email, "plan": plan}):
        return f"<h2>{email} is already subscribed to the {plan} plan.</h2>"
    subs_col.insert_one({"email": email, "plan": plan})
    return f"<h2>Subscription successful for {email} on the {plan} plan.</h2>"
