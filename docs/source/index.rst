LMPF Documentation
==================

Welcome to the **Labor Market and Population Forecasting (LMPF) Toolkit**  
The all-in-one solution for analyzing labor force trends, forecasting GDP impact, and managing user subscriptions and payments—built on FastAPI, securely backed by MongoDB Atlas, and deployed with Railway for robust, scalable cloud infrastructure.

.. contents:: Table of Contents
   :depth: 2
   :local:

Features
--------

- **Register:** Create your account with live field validation and strong password requirements.
- **Login:** Access your dashboard and analytics quickly, with immediate feedback on login attempts.
- **2FA (Two-Factor Authentication):** Add an extra layer of security using time-based one-time codes.
- **Profile Management:** View and update your profile, manage payments, and check subscription status.
- **Subscribe:** Explore and purchase subscription plans. Get instant confirmation of upgrades or error feedback.
- **Payment (BTC/PayPal):** Pay securely using Bitcoin or PayPal, with immediate transaction verification.
- **Password Reset:** Recover your account securely using email-based verification.
- **Cloud-Native Database:** All user, subscription, and payment data is stored in MongoDB Atlas, managed by Railway for reliability and scalability.

Live Demo Access
----------------

Try out the core features now—your data is instantly processed and stored in the cloud!

.. raw:: html

    <div style="margin:2em 0; text-align:center;">
        <button onclick="window.open('https://lmpf-production-a44c.up.railway.app/register', '_blank')" style="background: #0070f3; color: #fff; border: none; text-decoration: none; padding: 0.7em 2em; border-radius: 4px; font-size: 1.08em; margin: 0 1em; cursor: pointer;">Register (Live)</button>
        <button onclick="window.open('https://lmpf-production-a44c.up.railway.app/login', '_blank')" style="background: #28a745; color: #fff; border: none; text-decoration: none; padding: 0.7em 2em; border-radius: 4px; font-size: 1.08em; margin: 0 1em; cursor: pointer;">Login (Live)</button>
        <button onclick="window.open('https://lmpf-production-a44c.up.railway.app/subscribe', '_blank')" style="background: #9c27b0; color: #fff; border: none; text-decoration: none; padding: 0.7em 2em; border-radius: 4px; font-size: 1.08em; margin: 0 1em; cursor: pointer;">Subscribe (Live)</button>
        <a href="https://lmpf-production-a44c.up.railway.app/login" style="background: #28a745; color: #fff; text-decoration: none; padding: 0.7em 2em; border-radius: 4px; font-size: 1.08em; margin: 0 1em; display:inline-block;">Login (Live)</a>
        <a href="https://lmpf-production-a44c.up.railway.app/register" style="background: #0070f3; color: #fff; text-decoration: none; padding: 0.7em 2em; border-radius: 4px; font-size: 1.08em; margin: 0 1em; display:inline-block;">Register (Live)</a>
        <a href="https://lmpf-production-a44c.up.railway.app/subscribe" style="background: #9c27b0; color: #fff; text-decoration: none; padding: 0.7em 2em; border-radius: 4px; font-size: 1.08em; margin: 0 1em; display:inline-block;">Subscribe (Live)</a>
    </div>

How It Works
------------

1. **Register** with your email and password—instantly know if your username is taken or your password is too weak.
2. **Log in** to your dashboard; failed attempts return clear error messages.
3. **Enable 2FA** by scanning a QR code or entering a secret into your authenticator app.
4. **Subscribe** to a plan and review your details on your profile.
5. **Pay** securely with Bitcoin or PayPal; transactions are verified in real time.
6. **Access premium analytics and forecasting tools** as soon as payment is confirmed.
7. **All user, subscription, and payment data is stored securely in MongoDB Atlas, managed by Railway.**

Example FastAPI Endpoints
-------------------------

The following endpoints are live and connected to MongoDB Atlas:

- `/register`: Create a new account.
- `/login`: Log in to your account.
- `/subscribe`: Subscribe to a plan.

Example usage:
::
   - Registration form: POST /register with username, email, password
   - Login form: POST /login with username, password
   - Subscribe form: POST /subscribe with email, plan

(See the API Reference for more details and expected request/response formats.)

API Documentation
-----------------

- `API Reference <api.html>`__
- `Subscription & Payments API <subscription.html>`__
- `User Management API <user.html>`__

Support
-------

Need help? Contact our support team at `support@example.com`.

License
-------

MIT License
