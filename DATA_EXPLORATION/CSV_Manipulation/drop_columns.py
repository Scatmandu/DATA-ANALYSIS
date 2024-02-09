# Importing necessary libraries
import pandas as pd

# Specify the file path to your "Global_Superstore.csv" file
file_path = "Label_Encoded.csv"

# Loading the dataset
df = pd.read_csv(file_path)

# Make a copy of the DataFrame
df_copy = df.copy()

# Columns to ignore/drop
columns_to_drop = ['State', 'Country']

# Drop the specified columns from the copy
df_copy = df_copy.drop(columns=columns_to_drop)

# Save the modified DataFrame to a new CSV file
new_file_path = "Ready_for_One_Hot.csv"
df_copy.to_csv(new_file_path, index=False)

# Displaying the first few rows of the modified dataset
print(df_copy.head())

# Displaying information about the modified dataset
print(df_copy.info())

# Displaying general statistics about the modified numerical columns
print(df_copy.describe())
