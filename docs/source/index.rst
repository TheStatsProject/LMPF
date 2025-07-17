LMPF: Labor Market and Population Forecasting
=============================================

.. raw:: html

    <header style="background: #003366; color: #fff; padding: 2em 1em 1em 1em; text-align: center; border-radius: 10px 10px 0 0;">
        <h1>LMPF: Labor Market and Population Forecasting</h1>
        <p style="font-size:1.2em; max-width:670px; margin: 0 auto;">
            Analyze the impact of foreign-born populations on the U.S. economy by integrating demographic and economic data. 
            LMPF provides interactive analytics and visualizations for labor force participation and GDP contributions.
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

About the Project
-----------------

**LMPF** (Labor Market and Population Forecasting) is a Python-based toolkit for analyzing labor market participation and GDP contributions by native and foreign-born populations in the United States. 
It integrates datasets from the U.S. Census Bureau and the Federal Reserve Economic Data (FRED) to provide robust analytics and visualizations. The project empowers researchers, policymakers, and data scientists to understand and forecast the economic impact of migration.

.. _features:

Key Features
------------

.. raw:: html

    <div style="background: #e9f2fb; border-left: 4px solid #003366; margin: 1.2em 0; padding: 1em 1em 1em 1.5em; border-radius: 5px;">
        <b>Data Integration:</b>
        <ul>
            <li>Fetches demographic data from the U.S. Census Bureau's American Community Survey (ACS).</li>
            <li>Retrieves economic series from the FRED API.</li>
        </ul>
    </div>
    <div style="background: #e9f2fb; border-left: 4px solid #003366; margin: 1.2em 0; padding: 1em 1em 1em 1.5em; border-radius: 5px;">
        <b>Labor Market and GDP Analysis:</b>
        <ul>
            <li>Estimates labor force participation for native and foreign-born populations.</li>
            <li>Projects GDP contributions using workforce and economic growth data.</li>
        </ul>
    </div>
    <div style="background: #e9f2fb; border-left: 4px solid #003366; margin: 1.2em 0; padding: 1em 1em 1em 1.5em; border-radius: 5px;">
        <b>Interactive Visualizations:</b>
        <ul>
            <li>Bar charts, pie charts, and polar plots powered by Plotly.</li>
            <li>Compare GDP contribution by migrant groups and visualize employment by industry.</li>
        </ul>
    </div>
    <div style="background: #e9f2fb; border-left: 4px solid #003366; margin: 1.2em 0; padding: 1em 1em 1em 1.5em; border-radius: 5px;">
        <b>Extensible Python Code:</b>
        <ul>
            <li>Core analysis provided as a Python script.</li>
            <li>Easy to adapt for custom research or additional data sources.</li>
        </ul>
    </div>

.. _visuals:

Sample Visualizations
---------------------

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

#. Clone the repository:
   
   .. code-block:: bash

      git clone https://github.com/TheStatsProject/LMPF.git

#. Install dependencies:

   .. code-block:: bash

      pip install requests pandas fredapi plotly

#. Set your API keys in the analysis script:

   - ``CENSUS_KEY = 'your_census_api_key_here'``
   - ``FRED_KEY = 'your_fred_api_key_here'``

#. Run the main analysis script:

   .. code-block:: bash

      python lmpf_analysis.py

.. _api:

API & Documentation
-------------------

- `API Reference <api.html>`__ (autosummary)
- `Full Analysis Report <My-art.html>`__
- `Repository Overview <My-art3.html>`__

Conclusion
----------

LMPF is a powerful tool for understanding the economic role of migration in the United States. The repository’s code and visualizations are designed for both rapid exploration and deep analysis. Future releases aim to expand the dataset coverage and analytical features.

.. raw:: html

    <div style="margin:2em 0; text-align:center;">
        <a href="/server/templates/login.html"
           style="background: #28a745; color: #fff; text-decoration: none; padding: 0.7em 2em; border-radius: 4px; font-size: 1.08em; margin-right:1em;">
            Get Access
        </a>
        <span style="font-size:1em; color:#d32f2f; margin-left:1em;">
            <a href="/server/templates/register.html" style="color:#d32f2f; text-decoration:underline; font-weight:bold;">
                Subscribe
            </a>
            for new users
        </span>
    </div>

.. raw:: html

    <div style="margin:2em 0; text-align:center;">
        <a href="/server/templates/login.html"
           style="background: #28a745; color: #fff; text-decoration: none; padding: 0.7em 2em; border-radius: 4px; font-size: 1.08em; margin-right:1em;">
            Get Access
        </a>
        <span style="font-size:1em; color:#d32f2f; margin-left:1em;">
            <a href="/server/templates/register.html" style="color:#d32f2f; text-decoration:underline; font-weight:bold;">
                Subscribe
            </a>
            for new users
        </span>
    </div>


.. raw:: html

    <div style="margin:2em 0; text-align:center;">
        <a href="https://lmpf-app.fly.dev/login"
           style="background: #28a745; color: #fff; text-decoration: none; padding: 0.7em 2em; border-radius: 4px; font-size: 1.08em; margin-right:1em;">
            Get Access
        </a>
        <span style="font-size:1em; color:#d32f2f; margin-left:1em;">
            <a href="https://lmpf-app.fly.dev/register" style="color:#d32f2f; text-decoration:underline; font-weight:bold;">
                Subscribe
            </a>
            for new users
        </span>
    </div>

.. raw:: html

    <div style="margin:2em 0; text-align:center;">
        <a href="login.html"
           style="background: #28a745; color: #fff; text-decoration: none; padding: 0.7em 2em; border-radius: 4px; font-size: 1.08em; margin-right:1em;">
            Get Access
        </a>
        <span style="font-size:1em; color:#d32f2f; margin-left:1em;">
            <a href="docs/server/register.html" style="color:#d32f2f; text-decoration:underline; font-weight:bold;">
                Subscribe
            </a>
            for new users
        </span>
    </div>


Login
=====

To access the secured documentation and tools, please use the official application:

:fa:`sign-in` **[Go to Login Page](https://lmpf-app.fly.dev/login)**

If you do not have an account, please [Subscribe here](register.html).

Subscribe / Register
====================

To create a new account, go to:

:fa:`user-plus` **[Register Here](https://lmpf-app.fly.dev/register)**

Already have an account? Go to [Login](login.html).
