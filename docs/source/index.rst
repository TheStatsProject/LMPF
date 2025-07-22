LMPF: Labor Market and Population Forecasting
=============================================

.. raw:: html

    <header style="background: #003366; color: #fff; padding: 2em 1em 1em 1em; text-align: center; border-radius: 10px 10px 0 0;">
        <h1>LMPF: Labor Market and Population Forecasting</h1>
        <p style="font-size:1.2em; max-width:670px; margin: 0 auto;">
            Analyze the impact of foreign-born populations on the U.S. economy with interactive analytics and visualizations. LMPF integrates trusted demographic and economic data for robust labor force and GDP analysis.
        </p>
    </header>
    <nav style="background: #f1f1f1; padding: 1em; text-align: center;">
        <a href="#about" style="margin: 0 1em; color: #003366; text-decoration: none; font-weight: 500;">About</a>
        <a href="#features" style="margin: 0 1em; color: #003366; text-decoration: none; font-weight: 500;">Features</a>
        <a href="#visuals" style="margin: 0 1em; color: #003366; text-decoration: none; font-weight: 500;">Visuals</a>
        <a href="#quickstart" style="margin: 0 1em; color: #003366; text-decoration: none; font-weight: 500;">Get Started</a>
        <a href="#api" style="margin: 0 1em; color: #003366; text-decoration: none; font-weight: 500;">API Docs</a>
        <a href="https://github.com/TheStatsProject/LMPF" target="_blank" style="margin: 0 1em; color: #003366; text-decoration: none; font-weight: 500;">GitHub</a>
    </nav>

.. _about:

About LMPF
----------

**LMPF** is a Python toolkit for analyzing the labor market and GDP impact of native and foreign-born populations in the United States.  
It integrates U.S. Census Bureau and Federal Reserve Economic Data (FRED) for policy, research, and data science applications.

.. _features:

Key Features
------------

.. raw:: html

    <div style="background: #e9f2fb; border-left: 4px solid #003366; margin: 1.2em 0; padding: 1em 1em 1em 1.5em; border-radius: 5px;">
        <b>Data Integration:</b>
        <ul>
            <li>Fetches demographic data from ACS and economic series from FRED.</li>
        </ul>
        <b>Labor Market & GDP Analytics:</b>
        <ul>
            <li>Labor force participation and GDP projections by group.</li>
        </ul>
        <b>Interactive Visuals:</b>
        <ul>
            <li>Plotly-powered charts comparing groups and industries.</li>
        </ul>
        <b>Extensible Python Code:</b>
        <ul>
            <li>Modular analysis scripts for custom research.</li>
        </ul>
    </div>

.. _visuals:

Visuals
-------

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
        <p style="font-size:0.97em; color: #444;">U.S. GDP, 1947–Present</p>
    </div>
    <div style="margin: 2em 0; text-align: center;">
        <iframe src="_static/employed_by_industry_native_2022_polar.html" title="Native Employed by Industry (2022)" width="80%" height="400" style="border:none;"></iframe>
        <p style="font-size:0.97em; color: #444;">Native Employed by Industry (2022)</p>
    </div>

.. _quickstart:

Get Started
-----------

1. **Clone the repository:**
   
   .. code-block:: bash

      git clone https://github.com/TheStatsProject/LMPF.git

2. **Install dependencies:**

   .. code-block:: bash

      pip install requests pandas fredapi plotly

3. **Set your API keys:**

   - ``CENSUS_KEY = 'your_census_api_key'``
   - ``FRED_KEY = 'your_fred_api_key'``

4. **Run the analysis:**

   .. code-block:: bash

      python lmpf_analysis.py

.. _api:

API Docs
--------

- `API Reference <api.html>`__
- `Analysis Report <My-art.html>`__
- `Repository Overview <My-art3.html>`__

Access LMPF
-----------

Secure docs and analytics require a site account.  
**Register or log in using your site credentials.**  
*(No GitHub account required!)*

.. raw:: html

    <div style="margin:2em 0; text-align:center;">
        <a href="/login" style="background: #28a745; color: #fff; text-decoration: none; padding: 0.7em 2em; border-radius: 4px; font-size: 1.08em; margin-right:1em;">
            Login
        </a>
        <a href="/register" style="background: #0070f3; color: #fff; text-decoration: none; padding: 0.7em 2em; border-radius: 4px; font-size: 1.08em; margin-left:1em;">
            Register
        </a>
    </div>

Conclusion
----------

.. raw:: html

    <div style="margin:2em 0; text-align:center;">
        <a href="https://lmpf-backend.onrender.com/login" style="background: #28a745; color: #fff; text-decoration: none; padding: 0.7em 2em; border-radius: 4px; font-size: 1.08em; margin-right:1em;">
            Login
        </a>
        <a href="https://lmpf-backend.onrender.com/register" style="background: #0070f3; color: #fff; text-decoration: none; padding: 0.7em 2em; border-radius: 4px; font-size: 1.08em; margin-left:1em;">
            Register
        </a>
    </div>

LMPF empowers exploration and forecasting of the economic role of migration in the U.S.  
The toolkit and visualizations support both quick insights and deep dives.  
Stay tuned for expanded datasets and features.
