"Economic Insights: The Untold Story of Mexican Migrant Labor and Their Transformative Impact on U.S. GDP—Unpacking President Sheinbaum's Bold Assertions"
============================================================

In a time when misinformation spreads faster than facts, separating myth from reality has never been more crucial. Following President Claudia Sheinbaum's recent `comments <https://www.gob.mx/presidencia/prensa/las-y-los-migrantes-contribuyen-a-la-economia-de-estados-unidos-presidenta-claudia-sheinbaum-en-2024-aportaron-al-pib-781-mil-mdd>`_ on employment, migration, foreign trade, and economic history, a vital question resurfaces:

What is the true economic impact of Mexican immigrants in the United States?

To answer this question, we went straight to the source by analyzing data from the `U.S. Census Bureau <https://www.census.gov/>`_ and the `Federal Reserve's FRED <https://fred.stlouisfed.org>`_ database. The findings we uncovered may challenge common narratives, and believe me, they will.

This is a fact-based analysis, based solely on official U.S. government sources. No opinions or manipulations, just the numbers that matter, just the raw facts. Nothing else, just science to restore balance.

---

Why This Analysis Matters
-------------------------

**Economic Transparency** 

- Offers a data-driven perspective on the role of migrant labor of Migrants in the U.S. economy.
- Highlights the importance of using data and science to debunk myths and misconceptions surrounding immigration.
- Facilitates informed discussions among policymakers, researchers, and the general public by presenting unbiased and factual insights.

**Policy Implications**

- Highlights the contributions of foreign-born workers to inform immigration and economic policies.
- Offers actionable insights to guide the development of balanced immigration and economic policies that maximize the potential of migrant labor.
- Identifies high-growth sectors, such as healthcare, agriculture, and construction, where migrant labor plays a pivotal role.

**Investor Insights**

- Identifies key sectors and demographics driving economic growth.
- Identifies high-growth sectors, such as healthcare, agriculture, and construction, where migrant labor plays a pivotal role.
- Highlights key demographic trends that drive economic productivity and consumer demand.

---

Methodology Overview: Measuring America's People and Economy
-------------------------

**Recommended Readings**
~~~~~~~~~~~~~~~~~~~~~~~~~~~


1. **Introductory/Basic Level**  
   *Introduction to the Economics of Immigration in OECD Countries*  
   **Author(s):** Institute of Labor Economics `Discussion Paper No. 13755 <https://docs.iza.org/dp13755.pdf?utm_source=chatgpt.com>`_

   This paper analyzes the impact of migration on the labor market and GDP in OECD countries. It explains in a simple way how to measure the contribution of immigrants to aggregate output, focusing on employment share rather than total population. Despite being a 2018 paper, it is a starting point for understanding the calculations developed.

2. **Intermediate/Medium Level**  
   *Rethinking the Benefits of Immigration: Theory and Evidence from the U.S.*  
   **Author(s):** Gianmarco I.P. Ottaviano and Giovanni Peri `NATIONAL BUREAU OF ECONOMIC RESEARCH Working Paper No. 11672 <https://www.nber.org/system/files/working_papers/w11672/w11672.pdf?utm_source=chatgpt.com>`_

   This work is another good reference for understanding the meaning of the calculations performed in this article. It develops a two-sector macroeconomic model where natives and immigrants are imperfect substitutes. It then uses data from the Census/American Community Survey—extremely similar to the way we constructed the database—to empirically estimate the contribution each worker makes to GDP.

3. **Advanced/Specialized Level**  
   *Immigration and Economic Growth*  
   **Author:** George J. Borjas `NATIONAL BUREAU OF ECONOMIC RESEARCH Working Paper 25836 <https://www.nber.org/system/files/working_papers/w25836/w25836.pdf?utm_source=chatgpt.com>`_

   This analysis provides a rigorous macro- and micro-level framework that links immigration inflows to changes in GDP growth rates and labor productivity, in close agreement with GDP projections for 2025 and GDP per worker that we estimated. It uses a formal model where :math:`GDP = f(K, L)`. to be linear-homogeneous. This allows for the decomposition of output per worker according to the proportion of native-born and immigrant workers, thereby making it possible to more accurately measure the sensitivity of the effects on GDP of an increase or decrease in immigrants.


**Data Sources**
~~~~~~~~~~~~~~~~~~~~~~~~~~~


1. **U.S. Census Bureau**: Provides population data for native and foreign-born groups.
2. **FRED ST Louis**: Supplies GDP and labor force participation rates.
3. **Custom Analysis**: Estimates GDP contributions by nationality based on labor force participation rates and official population statistics.

**Key Variables**
~~~~~~~~~~~~~~~~~~~~~~~~~~~


- **GDP_SERIES**: Real GDP series identifier (`GDPC1`).
- **MEX_LFP_SERIE**: Labor force participation rate for Mexican-born workers (`LNU01373395`).
- **ACS_YEARS**: List of years prioritizing the most recent available ACS data.
- **NATIVE_VAR**: Census variable for the number of native-born individuals in the U.S.
- **NFOREIGN_TOTAL**: Total number of foreign-born residents in the U.S. (all countries combined).
- **Ncountry_vars**: Dictionary mapping of countries to specific ACS variable codes.


**Steps**
~~~~~~~~~~~~~~~~~~~~~~~~~~~


- Fetch and analyze GDP data for 2024 and project it forward to 2025, the FRED series (“Real Gross Domestic Product”) is reported in chained 2017 dollars, meaning 2017  is the reference (base) year for the inflation‐adjusted series for this article.
- Estimate labor force participation for native and foreign-born populations.
- Calculate GDP contributions by nationality and project future trends.
- Visualize results through interactive charts and tables.

---

Key Findings: Migrant Myths vs. Reality
-------------------------

As we mentioned, we will analyze the statements made by President Claudia Sheinbaum through a report published on the Mexican government's official website, which you can consult `here <https://www.gob.mx/presidencia/prensa/las-y-los-migrantes-contribuyen-a-la-economia-de-estados-unidos-presidenta-claudia-sheinbaum-en-2024-aportaron-al-pib-781-mil-mdd>`_. Based on that report, we have found the following:

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
