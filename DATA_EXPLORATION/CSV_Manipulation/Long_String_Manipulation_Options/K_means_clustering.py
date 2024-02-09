import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

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

# Determine the number of clusters (you may need to experiment with this parameter)
num_clusters = 5

# Apply K-Means clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
feature_df['cluster'] = kmeans.fit_predict(feature_df)

# Save the clustered DataFrame to a new CSV file
output_file_path = "Clustered_Product_Names.csv"
feature_df.to_csv(output_file_path, index=False)

# Displaying the resulting DataFrame with clusters
print(feature_df.head())
