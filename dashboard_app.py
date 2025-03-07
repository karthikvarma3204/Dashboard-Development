 
import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("dashboard_dataset.csv")

# Initialize Dash app
app = dash.Dash(__name__)

# Create visualizations
fig_sales_trend = px.line(df, x="Date", y="Sales", title="Sales Trend Over Time")
fig_profit_category = px.bar(df, x="Category", y="Profit", title="Profit by Category", color="Category")
fig_sales_region = px.pie(df, names="Region", values="Sales", title="Sales Distribution by Region")

# Layout
app.layout = html.Div(children=[
    html.H1("Interactive Sales Dashboard", style={'textAlign': 'center'}),
    
    dcc.Graph(id="sales-trend", figure=fig_sales_trend),
    dcc.Graph(id="profit-category", figure=fig_profit_category),
    dcc.Graph(id="sales-region", figure=fig_sales_region)
])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
