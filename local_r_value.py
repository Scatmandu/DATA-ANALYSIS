import pandas as pd
from itertools import combinations
from scipy.stats import pearsonr

# Replace 'final_sanitized_data.csv' with your actual file path
file_path = 'final_sanitized_data.csv'

# Read the CSV file into a DataFrame
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    exit()

# Calculate and print Pearson's R for each combination of columns
columns = df.columns
correlations = []

for col1, col2 in combinations(columns, 2):
    r_value, _ = pearsonr(df[col1], df[col2])
    correlations.append((f"{col1}/{col2}", r_value))

# Sort correlations by the absolute value of the correlation coefficient (descending)
correlations.sort(key=lambda x: abs(x[1]), reverse=True)

# Print the sorted results
for pair, r_value in correlations:
    print(f"{pair} : r-value = {r_value}")
