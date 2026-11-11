# Sales & Profit Dashboard — Python Dash

A small analytics dashboard showing sales trends, category profitability, and sales distribution by region.

## Stack
Python, Dash, Plotly Express, pandas.

## Features
- Line chart: sales trend by date
- Bar chart: total profit by category
- Pie chart: regional sales distribution

## Run locally
```bash
python -m pip install -r requirements.txt
python dashboard_app.py
```
Visit http://127.0.0.1:8050.

The included `dashboard_dataset.csv` is sample data for demonstrating visualization. It is not live business data.

## Key files
- `dashboard_app.py`: Dash layout and Plotly charts
- `dashboard_dataset.csv`: illustrative sample records
- `requirements.txt`: packages required to run

## Limitations
This is a learning exercise, not a deployed analytics platform. It does not include user authentication, dynamic ingestion, or production monitoring.
