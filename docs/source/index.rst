LMPF Documentation
==================

Welcome to the Labor Market and Population Forecasting (LMPF) toolkit!  
Analyze labor force, GDP impact, and manage your secure subscription and payments.
Now seamlessly connects to MongoDB via Railway for robust data management and scalability.

.. contents:: Table of Contents
   :depth: 2
   :local:

Features
--------

- **Register:** Create a secure account with field-level validation and password strength checking.
- **Login:** Access your dashboard and analysis tools. Detailed error feedback for login attempts.
- **2FA (Two-Factor Authentication):** Enhance account security with time-based codes.
- **Profile:** Manage your account, payment status, and subscriptions.
- **Subscribe:** Choose and purchase a subscription plan. Receive instant feedback on errors and success.
- **Payment (BTC/PayPal):** Pay for your subscription using cryptocurrency or PayPal with transaction verification.
- **Password Reset:** Recover your account securely via email verification.
- **Database Integration:** All user, subscription, and payment data is stored securely in a MongoDB instance on Railway, ensuring reliability and scalability.

Quick Access to Forms
---------------------

Jump directly to core workflow templates for testing and development:

.. raw:: html

    <div style="margin:2em 0; text-align:center;">
        <button onclick="window.open('docs/server/templates/register.html', '_blank')" style="background: #0070f3; color: #fff; border: none; text-decoration: none; padding: 0.7em 2em; border-radius: 4px; font-size: 1.08em; margin: 0 1em; cursor: pointer;">Register Form (HTML)</button>
        <button onclick="window.open('docs/server/templates/login.html', '_blank')" style="background: #28a745; color: #fff; border: none; text-decoration: none; padding: 0.7em 2em; border-radius: 4px; font-size: 1.08em; margin: 0 1em; cursor: pointer;">Login Form (HTML)</button>
        <button onclick="window.open('docs/server/templates/subscribe.html', '_blank')" style="background: #9c27b0; color: #fff; border: none; text-decoration: none; padding: 0.7em 2em; border-radius: 4px; font-size: 1.08em; margin: 0 1em; cursor: pointer;">Subscribe Form (HTML)</button>
        <a href="/login" style="background: #28a745; color: #fff; text-decoration: none; padding: 0.7em 2em; border-radius: 4px; font-size: 1.08em; margin: 0 1em; display:inline-block;">Live Login</a>
        <a href="/register" style="background: #0070f3; color: #fff; text-decoration: none; padding: 0.7em 2em; border-radius: 4px; font-size: 1.08em; margin: 0 1em; display:inline-block;">Live Register</a>
        <a href="/subscribe" style="background: #9c27b0; color: #fff; text-decoration: none; padding: 0.7em 2em; border-radius: 4px; font-size: 1.08em; margin: 0 1em; display:inline-block;">Live Subscribe</a>
    </div>

How It Works
------------

1. **Register** with your email and password. Receive instant field-level error feedback if the username is taken or the password is weak.
2. **Login** to your dashboard with detailed error messages for unsuccessful attempts.
3. **Enable 2FA** for added security. Scan a QR code or enter your secret to use time-based codes.
4. **Subscribe** to a plan and receive clear feedback on your subscription and payment details.
5. **Pay** using BTC or PayPal, with support for transaction verification and error reporting.
6. **Access premium analytics and forecasting tools immediately after successful payment.
7. **All data is stored and managed in MongoDB, deployed and secured with Railway's cloud infrastructure.**

API Docs
--------

- `API Reference <api.html>`__
- `Subscription & Payments API <subscription.html>`__
- `User Management API <user.html>`__

Support
-------

Need help? Contact the support team at `support@example.com`.

License
-------

MIT License
