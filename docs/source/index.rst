LMPF: Labor Market and Population Forecasting
=============================================

.. raw:: html

    <header style="background: #003366; color: #fff; padding: 2em 1em 1em 1em; text-align: center; border-radius: 10px 10px 0 0;">
        <h1>LMPF: Labor Market and Population Forecasting</h1>
        <p style="font-size:1.2em; max-width:670px; margin: 0 auto;">
            Explore how foreign-born populations shape the U.S. economy. LMPF delivers interactive analytics and visualizations for labor force participation and GDP contributions, integrating demographic and economic data from trusted federal sources.
        </p>
    </header>
    <nav style="background: #f1f1f1; padding: 1em; text-align: center;">
        <a href="#about" style="margin: 0 1em; color: #003366; text-decoration: none; font-weight: 500;">About</a>
        <a href="#features" style="margin: 0 1em; color: #003366; text-decoration: none; font-weight: 500;">Features</a>
        <a href="#visuals" style="margin: 0 1em; color: #003366; text-decoration: none; font-weight: 500;">Sample Visuals</a>
        <a href="#quickstart" style="margin: 0 1em; color: #003366; text-decoration: none; font-weight: 500;">Getting Started</a>
        <a href="#api" style="margin: 0 1em; color: #003366; text-decoration: none; font-weight: 500;">API</a>
        <a href="https://github.com/TheStatsProject/LMPF" target="_blank" style="margin: 0 1em; color: #003366; text-decoration: none; font-weight: 500;">GitHub</a>
    </nav>

.. _about:

About LMPF
----------

**LMPF** (Labor Market and Population Forecasting) is a Python toolkit for analyzing the labor market and GDP impact of native and foreign-born populations in the United States.  
It unifies data from the U.S. Census Bureau and Federal Reserve Economic Data (FRED), giving researchers, policymakers, and data scientists robust tools to forecast and visualize the economic effects of migration and demographic change.

.. _features:

Key Features
------------

.. raw:: html

    <div style="background: #e9f2fb; border-left: 4px solid #003366; margin: 1.2em 0; padding: 1em 1em 1em 1.5em; border-radius: 5px;">
        <b>Comprehensive Data Integration:</b>
        <ul>
            <li>Automatically fetches demographic data from the U.S. Census Bureau's American Community Survey (ACS).</li>
            <li>Retrieves time-series economic indicators via the FRED API.</li>
        </ul>
    </div>
    <div style="background: #e9f2fb; border-left: 4px solid #003366; margin: 1.2em 0; padding: 1em 1em 1em 1.5em; border-radius: 5px;">
        <b>Labor Market and GDP Analytics:</b>
        <ul>
            <li>Estimates labor force participation for native and foreign-born groups.</li>
            <li>Projects GDP contributions and tracks workforce trends by cohort.</li>
        </ul>
    </div>
    <div style="background: #e9f2fb; border-left: 4px solid #003366; margin: 1.2em 0; padding: 1em 1em 1em 1.5em; border-radius: 5px;">
        <b>Interactive Visualizations:</b>
        <ul>
            <li>Bar charts, pie charts, and polar plots powered by Plotly for instant insight.</li>
            <li>Compare GDP impact by migrant group and visualize employment by industry.</li>
        </ul>
    </div>
    <div style="background: #e9f2fb; border-left: 4px solid #003366; margin: 1.2em 0; padding: 1em 1em 1em 1.5em; border-radius: 5px;">
        <b>Extensible Python Code:</b>
        <ul>
            <li>Modular analysis scripts easily adapted for custom research or additional data sources.</li>
            <li>Ready for integration into policy dashboards, academic studies, or enterprise analytics.</li>
        </ul>
    </div>

.. _visuals:

Sample Visualizations
--------------------

.. raw:: html

    <div style="margin: 2em 0; text-align: center;">
        <iframe src="_static/bar_2024.html" title="Top 10 Foreign-Born GDP Contribution" width="80%" height="420" style="border:none;"></iframe>
        <p style="font-size:0.97em; color: #444;">Top 10 Foreign-Born Groups by GDP Contribution (2024)</p>
    </div>
    <div style="margin: 2em 0; text-align: center;">
        <iframe src="_static/pie_2024.html" title="GDP Share by Foreign-Born Cohort" width="70%" height="400" style="border:none;"></iframe>
        <p style="font-size:0.97em; color: #444;">GDP Share by Foreign-Born Cohort (2024)</p>
    </div>
    <div style="margin: 2em 0; text-align: center;">
        <iframe src="_static/gdp_history.html" title="U.S. GDP Over Time" width="80%" height="340" style="border:none;"></iframe>
        <p style="font-size:0.97em; color: #444;">U.S. GDP, 1947–Present (FRED)</p>
    </div>
    <div style="margin: 2em 0; text-align: center;">
        <iframe src="_static/employed_by_industry_native_2022_polar.html" title="Native Employed by Industry (2022)" width="80%" height="400" style="border:none;"></iframe>
        <p style="font-size:0.97em; color: #444;">Native Employed by Industry (2022)</p>
    </div>

.. _quickstart:

Getting Started
---------------

1. **Clone the repository:**
   
   .. code-block:: bash

      git clone https://github.com/TheStatsProject/LMPF.git

2. **Install dependencies:**

   .. code-block:: bash

      pip install requests pandas fredapi plotly

3. **Set your API keys in the analysis script:**

   - ``CENSUS_KEY = 'your_census_api_key_here'``
   - ``FRED_KEY = 'your_fred_api_key_here'``

4. **Run the main analysis script:**

   .. code-block:: bash

      python lmpf_analysis.py

.. _api:

API & Documentation
-------------------

- `API Reference <api.html>`__ (autosummary)
- `Full Analysis Report <My-art.html>`__
- `Repository Overview <My-art3.html>`__

Access & Subscription
---------------------

Secure documentation and premium analytics require login.  
Create an account or sign in below to access all interactive tools and reports.

.. raw:: html

    <div style="margin:2em 0; text-align:center;">
        <a href="https://lmpf-app.fly.dev/login"
           style="background: #28a745; color: #fff; text-decoration: none; padding: 0.7em 2em; border-radius: 4px; font-size: 1.08em; margin-right:1em;">
            Login
        </a>
        <span style="font-size:1em; color:#d32f2f; margin-left:1em;">
            <a href="https://lmpf-app.fly.dev/register" style="color:#d32f2f; text-decoration:underline; font-weight:bold;">
                Register
            </a>
            for new users
        </span>
    </div>

Conclusion
----------

LMPF empowers you to explore, analyze, and forecast the economic role of migration in the U.S.  
The toolkit and visualizations are designed for both rapid exploration and deep analysis.  
Stay tuned for expanded datasets and advanced analytics in future releases.
