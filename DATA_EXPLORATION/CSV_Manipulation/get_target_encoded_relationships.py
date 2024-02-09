import pandas as pd

# Replace 'original_data.csv' and 'target_encoded_data.csv' with your actual file names
original_file_path = 'Ready_for_Target_Encoding.csv'
target_encoded_file_path = 'Final_Dataset.csv'

# Read the original and target-encoded CSV files into DataFrames
try:
    original_df = pd.read_csv(original_file_path)
    target_encoded_df = pd.read_csv(target_encoded_file_path)
except FileNotFoundError as e:
    print(f"Error: {e}")
    exit()

# List of categorical columns to compare
categorical_columns = ['Segment', 'Region', 'Category', 'Sub-Category']

# Create dictionaries to store mappings
mappings = {column: {} for column in categorical_columns}

# Iterate through each categorical column and compare original and target-encoded values
for categorical_column in categorical_columns:
    # Create a mapping dictionary for the current column
    mapping = dict(zip(original_df[categorical_column], target_encoded_df[categorical_column + '_encoded']))

    # Sort the mapping by numerical values in descending order
    sorted_mapping = dict(sorted(mapping.items(), key=lambda item: item[1], reverse=True))

    # Store the sorted mapping in the dictionary
    mappings[categorical_column] = sorted_mapping

    # Save the sorted mapping to a text file
    with open(f'{categorical_column}_mapping.txt', 'w') as file:
        for key, value in sorted_mapping.items():
            file.write(f"{key} = {value}\n")

print("Mappings saved to text files:")
for column in categorical_columns:
    print(f"{column}_mapping.txt")
