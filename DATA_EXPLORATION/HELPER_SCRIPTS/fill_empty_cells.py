import pandas as pd

# Replace 'input.csv' and 'output.csv' with your actual file paths
input_file_path = 'sanitized_data.csv'
output_file_path = 'final_sanitized_data.csv'

# Read the CSV file into a DataFrame
try:
    df = pd.read_csv(input_file_path)
except FileNotFoundError:
    print(f"Error: File '{input_file_path}' not found.")
    exit()

# Replace missing values with 69
df = df.fillna(69)

# Save the modified DataFrame to a new CSV file
df.to_csv(output_file_path, index=False)

print(f"CSV file with missing values replaced saved to '{output_file_path}'.")