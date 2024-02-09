import pandas as pd

# Replace 'new_data.csv' and 'newer_data.csv' with your actual file paths
input_file_path = 'new_data.csv'
output_file_path = 'newer_data.csv'

# Read the CSV file into a DataFrame
try:
    df = pd.read_csv(input_file_path)
except FileNotFoundError:
    print(f"Error: File '{input_file_path}' not found.")
    exit()


# Create a mapping dictionary for the GPUs
gpu_mapping = {
    'intel': 0,
    'nvidia': 1,
    'amd': 2,
    'mali': 3,
    'other': 4
}

# Apply the GPU mapping to the 'GPU' column
df['GPU'] = df['GPU'].apply(lambda x: gpu_mapping.get(x.lower(), x))

# Save the edited DataFrame to a new CSV file
df.to_csv(output_file_path, index=False)

print(f"Edited CSV saved to '{output_file_path}'.")
