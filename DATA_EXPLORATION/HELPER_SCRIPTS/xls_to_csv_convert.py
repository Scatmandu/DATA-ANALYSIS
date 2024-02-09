import pandas as pd

# Replace 'input_file.xls' and 'output_file.csv' with your actual file paths
input_file_path = 'GS.xls'
output_file_path = 'Global_Superstore.csv'

# Read the Excel file into a DataFrame
try:
    df = pd.read_excel(input_file_path)
except FileNotFoundError:
    print(f"Error: File '{input_file_path}' not found.")
    exit()

# Save the DataFrame to a CSV file
df.to_csv(output_file_path, index=False)

print(f"CSV file saved to '{output_file_path}'.")