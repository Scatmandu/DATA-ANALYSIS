import pandas as pd
import numpy as np
from scipy.stats import pearsonr, ttest_ind, f_oneway, chi2_contingency
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.seasonal import seasonal_decompose
import plotly.graph_objects as go

# Load the CSV file into a DataFrame
df = pd.read_csv('Final_Dataset.csv')

# Extract relevant columns
sales = df['Sales']
quantity = df['Quantity']
profit = df['Profit']
ship_mode = df['Ship Mode']
order_priority = df['Order Priority']
region_encoded = df['Region']
ship_time = pd.to_datetime(df['Ship Time'])

# Function to plot histograms
def plot_histogram(data, title, x_label, y_label):
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=data, histnorm='probability'))
    fig.update_layout(title=title, xaxis_title=x_label, yaxis_title=y_label)
    fig.show()

# Function to plot scatter plot
def plot_scatter(x, y, title, x_label, y_label):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='markers'))
    fig.update_layout(title=title, xaxis_title=x_label, yaxis_title=y_label)
    fig.show()

# 1. Mean (Average) - Histogram
plot_histogram(sales, 'Distribution of Sales', 'Sales', 'Probability')
plot_histogram(quantity, 'Distribution of Quantity', 'Quantity', 'Probability')
plot_histogram(profit, 'Distribution of Profit', 'Profit', 'Probability')

# 2. Correlation Coefficient (Pearson correlation coefficient) - Scatter plot
plot_scatter(quantity, sales, 'Sales vs Quantity', 'Quantity', 'Sales')
plot_scatter(profit, sales, 'Sales vs Profit', 'Profit', 'Sales')

# 3. Time Series Analysis (Seasonal Decomposition) - Line plot
decomposition = seasonal_decompose(sales, model='additive')
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

fig = go.Figure()
fig.add_trace(go.Scatter(x=ship_time, y=trend, mode='lines', name='Trend'))
fig.add_trace(go.Scatter(x=ship_time, y=seasonal, mode='lines', name='Seasonal'))
fig.add_trace(go.Scatter(x=ship_time, y=residual, mode='lines', name='Residual'))
fig.update_layout(title='Time Series Analysis (Seasonal Decomposition)',
                  xaxis_title='Date', yaxis_title='Value')
fig.show()
