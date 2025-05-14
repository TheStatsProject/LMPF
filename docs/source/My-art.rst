"Economic Insights: The Untold Story of Mexican Migrant Labor and Their Transformative Impact on U.S. GDP—Unpacking President Sheinbaum's Bold Assertions"
============================================================

In a time when misinformation spreads faster than facts, separating myth from reality has never been more crucial. Following President Claudia Sheinbaum's recent `comments <https://www.gob.mx/presidencia/prensa/las-y-los-migrantes-contribuyen-a-la-economia-de-estados-unidos-presidenta-claudia-sheinbaum-en-2024-aportaron-al-pib-781-mil-mdd>`_ on employment, migration, foreign trade, and economic history, a vital question resurfaces:

What is the true economic impact of Mexican immigrants in the United States?

To answer this question, we went straight to the source by analyzing data from the `U.S. Census Bureau <https://www.census.gov/>`_ and the `Federal Reserve's FRED <https://fred.stlouisfed.org>`_ database. The findings we uncovered may challenge common narratives, and believe me, they will.

This is a fact-based analysis, based solely on official U.S. government sources. No opinions or manipulations, just the numbers that matter, just the raw facts. Nothing else, just science to restore balance.

---

Why This Analysis Matters
-------------------------
- **Economic Transparency**: Offers a data-driven perspective on the role of migrant labor of Mexican Miigrants in the U.S. economy.
- **Policy Implications**: Highlights the contributions of foreign-born workers to inform immigration and economic policies.
- **Investor Insights**: Identifies key sectors and demographics driving economic growth.

---

Methodology Overview
~~~~~~~~~~~~~~~~~~~~

**Data Sources**

1. **Census Bureau API**: Provides population data for native and foreign-born groups.
2. **FRED API**: Supplies GDP and labor force participation rates.
3. **Custom Analysis**: Projects GDP contributions by nationality based on labor force participation.

**Key Variables**

- **CENSUS_KEY**: API key for accessing U.S. Census data.
- **FRED_KEY**: API key for accessing FRED economic data.
- **GDP_SERIES**: Real GDP series identifier (`GDPC1`).
- **MEX_LFP_SERIE**: Labor force participation rate for Mexican-born workers (`LNU01373395`).
- **ACS_YEARS**: List of years prioritizing the most recent available ACS data.

**Steps**
1. Fetch and analyze GDP data for 2024 and project it forward to 2025.
2. Estimate labor force participation for native and foreign-born populations.
3. Calculate GDP contributions by nationality and project future trends.
4. Visualize results through interactive charts and tables.

---

Key Findings
~~~~~~~~~~~~

1. **Migrant Labor Force Participation**
   - **Mexican-born workers**: Labor force participation rate of **{mex_lfp_rate:.2%}** for 2024.
   - **Active labor force**: Foreign-born workers contribute significantly to economic productivity.

2. **GDP Contributions**
   - **Total GDP (2024)**: USD **${GDP_2024:,.0f} billion**.
   - **Projected GDP (2025)**: USD **${GDP_2025:,.0f} billion** (assuming a growth rate of {GDP_GROWTH:.2%}).
   - **Foreign-born GDP share**: Significant contributions, with **top 15 migrant groups** highlighted below.

3. **Top 15 Migrant Groups by GDP Contribution**

.. list-table::
   :header-rows: 1

   * - Country
     - Active Labor Force
     - GDP Contribution (billion USD)
     - GDP/Worker (thousand USD)
   * - **Mexico**
     - {group_pop['Mexico']:,}
     - ${group_gdp['Mexico']:,.1f}
     - ${group_gdp_pc['Mexico']:,.1f}
   * - **India**
     - {group_pop['India']:,}
     - ${group_gdp['India']:,.1f}
     - ${group_gdp_pc['India']:,.1f}
   * - **China**
     - {group_pop['China']:,}
     - ${group_gdp['China']:,.1f}
     - ${group_gdp_pc['China']:,.1f}
   * - … (others in the top 15)

---

Interactive Visualizations
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Bar Chart: Top 10 Migrant Groups by GDP Contribution**

.. container:: dual-layout

   .. raw:: html

      <div style="display: flex;">
          <div style="width: 50%; padding-right: 10px;">
              <iframe src="_static/bar_2024.html" width="100%" height="400" style="border: none;">
                  Your browser does not support iframes. Please view the visualization directly at
                  <a href="_static/bar_2024.html">this link</a>.
              </iframe>
          </div>
          <div style="width: 50%; padding-left: 10px;">
              <p>
                  This bar chart highlights the top 10 migrant groups contributing to the U.S. GDP. 
                  Mexican and Indian-born workers lead the list, reflecting their strong labor force 
                  participation in key economic sectors. Hover over the bars to see detailed values.
              </p>
          </div>
      </div>

2. **Pie Chart: GDP Share by Migrant Cohort**

.. container:: dual-layout

   .. raw:: html

      <div style="display: flex;">
          <div style="width: 50%; padding-right: 10px;">
              <iframe src="_static/pie_2024.html" width="100%" height="400" style="border: none;">
                  Your browser does not support iframes. Please view the visualization directly at
                  <a href="_static/pie_2024.html">this link</a>.
              </iframe>
          </div>
          <div style="width: 50%; padding-left: 10px;">
              <p>
                  This pie chart illustrates the GDP share contributed by different migrant cohorts. 
                  It provides an at-a-glance understanding of how various groups impact the economy. 
                  Click on the chart segments to drill down into specific data points.
              </p>
          </div>
      </div>

---

Take Action
~~~~~~~~~~~

- **Policy Recommendations**: Invest in sectors with high migrant labor participation (e.g., healthcare, construction).
- **Investor Opportunities**: Develop bilingual consumer platforms to capture market share.
- **Future Research**: Extend analysis to other demographic groups and forecast long-term trends.

---

*All charts are live embeds—hover, zoom, and explore the data yourself!*
