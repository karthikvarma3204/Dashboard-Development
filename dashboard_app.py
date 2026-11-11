"""Simple sales and profit analytics dashboard built with Dash."""
from pathlib import Path
import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

ROOT = Path(__file__).resolve().parent
df = pd.read_csv(ROOT / "dashboard_dataset.csv", parse_dates=["Date"])
sales_by_date = df.groupby("Date", as_index=False)["Sales"].sum().sort_values("Date")
profit_by_category = df.groupby("Category", as_index=False)["Profit"].sum()
sales_by_region = df.groupby("Region", as_index=False)["Sales"].sum()

app = dash.Dash(__name__)
app.title = "Sales & Profit Dashboard"
app.layout = html.Div(
    style={"fontFamily": "Arial, sans-serif", "maxWidth": "1100px", "margin": "auto", "padding": "24px", "background": "#f8fafc"},
    children=[
        html.H1("Sales & Profit Dashboard"),
        html.P("Explore illustrative sales performance by date, product category, and region."),
        html.Div(
            style={"display": "flex", "gap": "16px", "flexWrap": "wrap"},
            children=[
                html.Div([html.Small("Total sales"), html.H2(f"{df['Sales'].sum():,.0f}")], style={"background": "white", "padding": "20px", "flex": "1", "borderRadius": "12px"}),
                html.Div([html.Small("Total profit"), html.H2(f"{df['Profit'].sum():,.0f}")], style={"background": "white", "padding": "20px", "flex": "1", "borderRadius": "12px"}),
                html.Div([html.Small("Records"), html.H2(f"{len(df):,}")], style={"background": "white", "padding": "20px", "flex": "1", "borderRadius": "12px"}),
            ],
        ),
        dcc.Graph(figure=px.line(sales_by_date, x="Date", y="Sales", title="Sales trend over time")),
        dcc.Graph(figure=px.bar(profit_by_category, x="Category", y="Profit", title="Total profit by category")),
        dcc.Graph(figure=px.pie(sales_by_region, names="Region", values="Sales", title="Sales by region")),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
