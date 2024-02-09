import pandas as pd

# Replace 'Ready_for_One_Hot.csv' with your actual CSV file name
csv_file_path = 'Ready_for_One_Hot.csv'

# Read the CSV file into a DataFrame
try:
    df = pd.read_csv(csv_file_path)
except FileNotFoundError:
    print(f"Error: File '{csv_file_path}' not found.")
    exit()

# Perform one-hot encoding on the specified columns
df = pd.get_dummies(df, columns=['Segment', 'Region', 'Category', 'Sub-Category'])

# Save the modified DataFrame to a new CSV file
output_file_path = 'Final_Dataset.csv'
df.to_csv(output_file_path, index=False)

print(f"One-hot encoded DataFrame saved to '{output_file_path}'.")
