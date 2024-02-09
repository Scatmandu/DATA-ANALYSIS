import pandas as pd

# Replace 'data.csv' with your actual CSV file name
csv_file_path = 'Ready_for_Target_Encoding.csv'

# Read the CSV file into a DataFrame
try:
    df = pd.read_csv(csv_file_path)
except FileNotFoundError:
    print(f"Error: File '{csv_file_path}' not found.")
    exit()

# List of categorical columns to target encode
categorical_columns = ['Segment', 'Region', 'Category', 'Sub-Category']

# Iterate through each categorical column and perform target encoding
for categorical_column in categorical_columns:
    # Calculate the mean of the target variable for each category
    target_means = df.groupby(categorical_column)['Sales'].mean()

    # Map the mean values to the original DataFrame
    df[categorical_column + '_encoded'] = df[categorical_column].map(target_means)

# Drop the original categorical columns
df.drop(categorical_columns, axis=1, inplace=True)

# Save the modified DataFrame to a new CSV file
output_file_path = 'Final_Dataset.csv'
df.to_csv(output_file_path, index=False)

print(f"Target-encoded data saved to '{output_file_path}'.")
