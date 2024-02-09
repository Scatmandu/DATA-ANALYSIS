import pandas as pd

# Replace 'data.csv' with your actual CSV file name
csv_file_path = 'newer_data.csv'

# Read the CSV file into a DataFrame
try:
    df = pd.read_csv(csv_file_path)
except FileNotFoundError:
    print(f"Error: File '{csv_file_path}' not found.")
    exit()

# Extract the chosen column
condition_column = df['SSD Capacity']

# Save the extracted column to a text file
output_file_path = 'column.txt'
condition_column.to_csv(output_file_path, index=False, header=False)

print(f"Condition column saved to '{output_file_path}'.")
