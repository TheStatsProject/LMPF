LMPF Documentation
==================

Welcome to the **Labor Market and Population Forecasting (LMPF) Toolkit**  
Empowering you to analyze labor force trends, forecast GDP impact, and manage secure subscriptions and payments—all seamlessly connected to MongoDB via Railway for robust, scalable data management.

.. contents:: Table of Contents
   :depth: 2
   :local:

Features
--------

- **Register:** Secure account creation with real-time field validation and strong password enforcement.
- **Login:** Fast access to your dashboard and analytics, with detailed feedback for every login attempt.
- **2FA (Two-Factor Authentication):** Heightened security via time-based one-time codes.
- **Profile Management:** View and update your account, payment status, and subscriptions.
- **Subscribe:** Browse and purchase subscription plans; receive instant feedback on errors or successful upgrades.
- **Payment (BTC/PayPal):** Flexible payment options with instant transaction verification.
- **Password Reset:** Easily recover your account through secure email verification.
- **Cloud-Native Database:** All user, subscription, and payment data is securely stored in a MongoDB Atlas database managed by Railway, ensuring reliability and scalability.

Quick Access to Live Forms
--------------------------

Start using the live demo right away:

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

1. **Register** with your email and password—receive instant feedback if your username is taken or your password is weak.
2. **Log in** to your dashboard; unsuccessful attempts return clear error messages.
3. **Enable 2FA** for your account by scanning a QR code or entering a secret into your authenticator app.
4. **Subscribe** to a plan and review your subscription and payment details on your profile.
5. **Pay** securely using Bitcoin or PayPal, with real-time transaction verification and error reporting.
6. **Access premium analytics and forecasting tools** immediately after successful payment.
7. **All data is stored securely in MongoDB Atlas, managed by Railway's cloud infrastructure.**

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
