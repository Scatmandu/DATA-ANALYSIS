import pandas as pd
import numpy as np
from scipy.stats import pearsonr, ttest_ind
from sklearn.linear_model import LinearRegression

# Load the CSV file into a DataFrame
df = pd.read_csv('Final_Dataset.csv')

# Extract relevant columns
sales = df['Sales']
quantity = df['Quantity']
profit = df['Profit']

# 1. Mean (Average)
sales_mean = np.mean(sales)
quantity_mean = np.mean(quantity)
profit_mean = np.mean(profit)
print("Mean (Average) - Sales:", sales_mean)
print("Mean (Average) - Quantity:", quantity_mean)
print("Mean (Average) - Profit:", profit_mean)

# 2. Standard Deviation
sales_std = np.std(sales)
quantity_std = np.std(quantity)
profit_std = np.std(profit)
print("\nStandard Deviation - Sales:", sales_std)
print("Standard Deviation - Quantity:", quantity_std)
print("Standard Deviation - Profit:", profit_std)

# 3. Correlation Coefficient (Pearson correlation coefficient)
sales_quantity_corr, _ = pearsonr(sales, quantity)
sales_profit_corr, _ = pearsonr(sales, profit)
print("\nCorrelation Coefficient (Sales vs Quantity):", sales_quantity_corr)
print("Correlation Coefficient (Sales vs Profit):", sales_profit_corr)

# 4. Regression Analysis
X = quantity.values.reshape(-1, 1)
y = sales.values.reshape(-1, 1)
regression_model = LinearRegression().fit(X, y)
slope = regression_model.coef_[0][0]
intercept = regression_model.intercept_[0]
print("\nRegression Analysis - Slope (Quantity vs Sales):", slope)
print("Regression Analysis - Intercept (Quantity vs Sales):", intercept)

# 5. Hypothesis Testing (t-test)
sales_high_discount = df[df['Discount'] > 0]['Sales']
sales_no_discount = df[df['Discount'] == 0]['Sales']
t_stat, p_value = ttest_ind(sales_high_discount, sales_no_discount)
print("\nHypothesis Testing (t-test) - t-statistic:", t_stat)
print("Hypothesis Testing (t-test) - p-value:", p_value)
