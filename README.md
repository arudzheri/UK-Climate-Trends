# UK Historic Weather Statistical Analysis

This repository contains a clean historical dataset of UK annual mean temperatures (1884–2025) and a full statistical analysis notebook exploring long-term climate trends.

## 📁 Dataset: `data/uk-mean-temperature.csv`

**Columns:**
- `Year` — Calendar year (1884–2025)
- `Annual_Mean_Temperature_C` — Mean annual temperature in °C

The dataset is sourced from long-term UK climate records and cleaned for direct use in statistical modelling.

## Data source

The annual mean temperature series was downloaded from the Met Office UK climate records and temperature data archive:
https://www.metoffice.gov.uk/research/climate/maps-and-data/uk-and-ireland-temperature-data

## 📊 Notebook: `uk_historic_weather_statistical_analysis.ipynb`

The notebook includes:

- Data loading and preprocessing  
- Exploratory data analysis  
- Trend visualisation  
- Linear regression modelling  
- ARIMA time-series forecasting  
- Climate insights and conclusions  

## Key results

- The linear trend shows warming of about 0.10 °C per decade.
- The mean temperature for 1884–1913 was 8.03 °C, versus 9.32 °C for 1996–2025, a difference of about 1.29 °C.
- All ten warmest years in the record occurred after 2000.
- The ARIMA(2,1,2) forecast remains close to 9.7 °C, which indicates that this simple model does not capture the long-term warming trend well.

## 🔧 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```
