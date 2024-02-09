import pandas as pd

def remove_columns(csv_path, output_path, columns_to_remove):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_path)

        # Check if the specified columns exist
        for column_name in columns_to_remove:
            if column_name not in df.columns:
                print(f"Error: Column '{column_name}' not found in the CSV.")
                return

        # Remove the specified columns along with their data
        df = df.drop(columns=columns_to_remove)

        # Save the DataFrame to a new CSV file
        df.to_csv(output_path, index=False)

        print(f"Columns {columns_to_remove} and their data removed. New CSV saved to '{output_path}'.")
    except FileNotFoundError:
        print(f"Error: File '{csv_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# Replace 'input.csv', 'output.csv', and ['column1', 'column2'] with your actual file paths and column names
remove_columns('newer_data.csv', 'sanitized_data.csv', ['Currency', 'Condition Description', 'Seller Note', 'Processor', 'Processor Speed', 'Processor Speed Unit', 'Type', 'Width of the Display', 'Height of the Display', 'Screen Size (inch)', 'SSD Capacity Unit', 'Ram Size Unit', 'Hard Drive Capacity Unit'])
