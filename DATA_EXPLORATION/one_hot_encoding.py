# Importing necessary libraries
import pandas as pd

# Specify the file path to your "Global_Superstore.csv" file
file_path = "New_Global_Superstore.csv"

# Loading the dataset
df = pd.read_csv(file_path)

# Make a copy of the DataFrame
df_copy = df.copy()

# Columns to ignore/drop
columns_to_drop = ['Row ID', 'Customer ID', 'Customer Name', 'City', 'Market', 'Product ID', 'Postal Code']

# Drop the specified columns from the copy
df_copy = df_copy.drop(columns=columns_to_drop)

# Encode 'Ship Mode' using one-hot encoding
df_copy = pd.get_dummies(df_copy, columns=['Ship Mode'], prefix='Ship_Mode')

# Displaying the first few rows of the modified dataset
print(df_copy.head())

# Displaying information about the modified dataset
print(df_copy.info())

# Displaying general statistics about the modified numerical columns
print(df_copy.describe())
