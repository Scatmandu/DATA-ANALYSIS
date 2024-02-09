# Importing necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Specify the file path to your "Dropped_Columns.csv" file
file_path = "Dropped_Columns.csv"

# Loading the dataset
df = pd.read_csv(file_path)

# Define a LabelEncoder
label_encoder = LabelEncoder()

# Apply label encoding to 'Ship Mode' and 'Order Priority'
df['Ship Mode'] = label_encoder.fit_transform(df['Ship Mode'])
df['Order Priority'] = label_encoder.fit_transform(df['Order Priority'])

# Save the modified DataFrame to a new CSV file
label_encoded_file_path = "Label_Encoded.csv"
df.to_csv(label_encoded_file_path, index=False)

# Displaying the first few rows of the modified dataset
print(df.head())
