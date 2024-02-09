import pandas as pd
import detect_encoding

def read_csv_with_encoding(file_path):
    # Use chardet to detect the encoding of the file
    with open(file_path, 'rb') as f:
        result = detect_encoding.detect(f.read())

    # Display detected encoding
    detected_encoding = result['encoding']
    print(f"Detected Encoding: {detected_encoding}")

    # Read CSV with the detected encoding
    df = pd.read_csv(file_path, encoding=detected_encoding)

    # Convert DataFrame to Latin-1 encoding
    df_encoded = df.applymap(lambda x: x.encode('latin1', 'ignore').decode('latin1') if isinstance(x, str) else x)

    return df_encoded

# Replace 'your_dataset.csv' with your actual dataset file
csv_file_path = 'input.csv'

# Read CSV with encoding detection and conversion to Latin-1
df = read_csv_with_encoding(csv_file_path)

# Print the first few rows of the DataFrame to verify
print(df.head())
