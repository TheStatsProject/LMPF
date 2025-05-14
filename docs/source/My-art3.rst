Repository Overview: LMPF
=========================

This document provides an overview of the Labor Market and Population Forecasting (LMPF) repository. The repository focuses on analyzing the contributions of foreign-born populations to the U.S. economy. The codebase integrates data from multiple sources, including the U.S. Census Bureau and the Federal Reserve Economic Data (FRED), to estimate active labor force participation and GDP contributions. The provided Python script is fully functional and serves as the core implementation for these analyses.

Key Features
------------

1. **Data Integration**:
   - Fetches data from the U.S. Census Bureau's American Community Survey (ACS).
   - Retrieves economic time series data from the Federal Reserve Economic Data (FRED) API.

2. **Labor Market and GDP Analysis**:
   - Estimates active labor force participation rates for native and foreign-born populations.
   - Projects GDP contributions based on workforce participation and economic growth rates.

3. **Visualizations**:
   - Generates interactive tables, bar charts, and pie charts using Plotly.
   - Compares GDP contributions of migrant groups with global economies.

Getting Started
---------------

### Prerequisites
To run the script, ensure you have the following Python libraries installed:

- `requests`
- `pandas`
- `fredapi`
- `plotly`

You can install these dependencies using pip:

```bash
pip install requests pandas fredapi plotly
```

### API Keys
Replace the placeholders in the script with your own API keys for the U.S. Census Bureau and FRED:

```python
CENSUS_KEY = 'your_census_api_key_here'
FRED_KEY = 'your_fred_api_key_here'
```

### Running the Script
Save the script as `lmpf_analysis.py` and execute it using Python:

```bash
python lmpf_analysis.py
```

Script Overview
---------------

### Configuration
The script initializes API keys and configurations for accessing data and performing calculations. Key variables include:

- **ACS_YEARS**: Defines the years of the ACS data to query.
- **GDP_SERIES**: The series ID for U.S. GDP data.
- **MEX_LFP_SERIE**: The series ID for labor force participation rates of Mexican-born individuals.

### Data Fetching

#### fetch_json(url, params)
Safely fetches JSON data from a URL with error handling:

```python
def fetch_json(url, params):
    """Safely fetch JSON data from a URL with error handling."""
    try:
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Request failed: {e}")
        print(f"[DEBUG] URL: {resp.url}")
        return None
```

#### get_working_acs_url()
Identifies the most recent year of the ACS data that can be successfully queried:

```python
def get_working_acs_url():
    for year in ACS_YEARS:
        url = f'https://api.census.gov/data/{year}/acs/acs1'
        test = fetch_json(url, {'get': 'NAME', 'for': 'us:1', 'key': CENSUS_KEY})
        if test:
            print(f"[INFO] Using ACS Year: {year}")
            return url, year
    raise RuntimeError("No working ACS year found!")
```

### Labor Market and GDP Calculations

1. **GDP Projections**:
   - Fetches the U.S. GDP for 2024 and projects GDP for 2025 based on growth rates.

2. **Labor Force Participation**:
   - Analyzes the labor force participation rates of foreign-born populations, with a focus on country-specific cohorts.

3. **Country-Specific Analyses**:
   - Fetches and processes data on the active labor force and GDP contributions for foreign-born populations from countries like Mexico, India, China, etc.

4. **Top Migrant Groups**:
   - Identifies the top 15 foreign-born groups contributing to the U.S. GDP.

5. **Projections for 2025**:
   - Projects labor force and GDP contributions for 2025 based on economic growth rates.

### Visualization
The script generates the following visualizations using Plotly:

1. **Table**:
   Displays the top 15 foreign-born groups by GDP contribution for 2024.

2. **Bar Chart**:
   Highlights the top 10 foreign-born groups by GDP contribution for 2024.

3. **Pie Chart**:
   Visualizes the GDP share of foreign-born cohorts for 2024.

4. **Comparison with Global Economies**:
   Compares the GDP contributions of foreign-born cohorts with the GDPs of major world economies.

Sample Visualizations
---------------------

### Table: Top 15 Foreign-Born Groups by GDP Contribution (2024)
This table shows the labor force size, GDP contribution, and GDP per worker for the top 15 foreign-born groups.

| Country       | Labor Force | GDP (bn USD) | GDP/Worker (kUSD) |
|---------------|-------------|--------------|-------------------|
| Mexico        | 10,000,000  | 500.0        | 50.0              |
| India         | 5,000,000   | 300.0        | 60.0              |
| ...           | ...         | ...          | ...               |

### Bar Chart: Top 10 Foreign-Born Groups by GDP Contribution (2024)
This bar chart highlights the GDP contributions of the top 10 foreign-born groups.

### Pie Chart: GDP Share by Foreign-Born Cohort (2024)
This pie chart provides a breakdown of GDP contributions by foreign-born cohorts.

### Comparison with Global Economies
This bar chart compares the GDP contributions of the top foreign-born groups with the GDPs of major world economies like the USA, China, Germany, and India.

Conclusion
----------

The LMPF repository is a powerful tool for understanding the economic contributions of foreign-born populations to the U.S. economy. By integrating data from multiple sources and leveraging advanced visualization techniques, the repository provides a detailed analysis of labor force participation and GDP contributions. Future enhancements could include projections for additional years and an expanded analysis of global migration trends.
