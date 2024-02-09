import DATA_EXPLORATION.HELPER_SCRIPTS.detect_encoding as detect_encoding

# Replace 'your_file_path' with the path to your file
file_path = 'input.csv'

# Function to detect encoding
def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        result = detect_encoding.detect(file.read())
    return result['encoding']

# Example usage
encoding = detect_encoding(file_path)
print(f"The detected encoding is: {encoding}")
