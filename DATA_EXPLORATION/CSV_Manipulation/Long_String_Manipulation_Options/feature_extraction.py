# Importing necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Specify the file path to your "Global_Superstore.csv" file
file_path = "Drop_Columns.csv"

# Loading the dataset
df = pd.read_csv(file_path)

# Extracting features from the "Product Name" column
product_names = df['Product Name']

# Initialize the CountVectorizer
vectorizer = CountVectorizer()

# Fit and transform the product names
product_name_features = vectorizer.fit_transform(product_names)

# Convert the result to a DataFrame for better visualization
feature_df = pd.DataFrame(product_name_features.toarray(), columns=vectorizer.get_feature_names_out())

# Save the resulting DataFrame to a CSV file
output_file_path = "Product_Name_Feature_Extract.csv"
feature_df.to_csv(output_file_path, index=False)

# Displaying the resulting DataFrame with extracted features
print(feature_df.head())
