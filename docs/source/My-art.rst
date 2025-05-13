## 🔍 Economic Insights: Migrant Labor Force and GDP Contributions

This section provides an in-depth analysis of U.S. labor force participation and GDP contributions by foreign-born populations, powered by data from the U.S. Census Bureau and the Federal Reserve Economic Data (FRED) API.

---

### 📋 Why This Analysis Matters
- **Economic Transparency**: Offers a data-driven perspective on the role of migrant labor in the U.S. economy.
- **Policy Implications**: Highlights the contributions of foreign-born workers to inform immigration and economic policies.
- **Investor Insights**: Identifies key sectors and demographics driving economic growth.

---

### 🔑 Methodology Overview

#### Data Sources
1. **Census Bureau API**: Provides population data for native and foreign-born groups.
2. **FRED API**: Supplies GDP and labor force participation rates.
3. **Custom Analysis**: Projects GDP contributions by nationality based on labor force participation.

#### Key Variables
- **CENSUS_KEY**: API key for accessing U.S. Census data.
- **FRED_KEY**: API key for accessing FRED economic data.
- **GDP_SERIES**: Real GDP series identifier (`GDPC1`).
- **MEX_LFP_SERIE**: Labor force participation rate for Mexican-born workers (`LNU01373395`).
- **ACS_YEARS**: List of years prioritizing the most recent available ACS data.

#### Steps
1. Fetch and analyze GDP data for 2024 and project it forward to 2025.
2. Estimate labor force participation for native and foreign-born populations.
3. Calculate GDP contributions by nationality and project future trends.
4. Visualize results through interactive charts and tables.

---

### 📊 Key Findings

#### 1. Migrant Labor Force Participation
- **Mexican-born workers**: Labor force participation rate of **{mex_lfp_rate:.2%}** for 2024.
- **Active labor force**: Foreign-born workers contribute significantly to economic productivity.

#### 2. GDP Contributions
- **Total GDP (2024)**: USD **${GDP_2024:,.0f} billion**.
- **Projected GDP (2025)**: USD **${GDP_2025:,.0f} billion** (assuming a growth rate of {GDP_GROWTH:.2%}).
- **Foreign-born GDP share**: Significant contributions, with **top 15 migrant groups** highlighted below.

#### 3. Top 15 Migrant Groups by GDP Contribution
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

### 📈 Interactive Visualizations

#### 1. Bar Chart: Top 10 Migrant Groups by GDP Contribution
.. raw:: html

   <div style="width:100%; height:400px;">
     <script src="https://cdn.plot.ly/plotly-2.32.0.min.js"></script>
     <div id="bar-top10" style="height:100%; width:100%;"></div>
     <script>
       Plotly.newPlot("bar-top10", /* data + layout loaded from bar_chart.json */);
     </script>
   </div>

#### 2. Pie Chart: GDP Share by Migrant Cohort
.. raw:: html

   <div style="width:100%; height:400px;">
     <script src="https://cdn.plot.ly/plotly-2.32.0.min.js"></script>
     <div id="pie-2024" style="height:100%; width:100%;"></div>
     <script>
       Plotly.newPlot("pie-2024", /* data + layout loaded from pie_chart.json */);
     </script>
   </div>

#### 3. Comparison: Migrant Groups vs. World GDPs
.. raw:: html

   <div style="width:100%; height:400px;">
     <script src="https://cdn.plot.ly/plotly-2.32.0.min.js"></script>
     <div id="comp-gdp" style="height:100%; width:100%;"></div>
     <script>
       Plotly.newPlot("comp-gdp", /* data + layout loaded from comparison_chart.json */);
     </script>
   </div>

---

### 🚀 Take Action
- **Policy Recommendations**: Invest in sectors with high migrant labor participation (e.g., healthcare, construction).
- **Investor Opportunities**: Develop bilingual consumer platforms to capture market share.
- **Future Research**: Extend analysis to other demographic groups and forecast long-term trends.

---

*All charts are live embeds—hover, zoom, and explore the data yourself!*
