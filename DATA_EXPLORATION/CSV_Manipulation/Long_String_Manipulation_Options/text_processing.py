# Importing necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download NLTK resources (if not downloaded)
nltk.download('punkt')
nltk.download('wordnet')

# Specify the file path to your "Global_Superstore.csv" file
file_path = "Drop_Columns.csv"

# Loading the dataset
df = pd.read_csv(file_path)

# Extracting features from the "Product Name" column
product_names = df['Product Name']

# Tokenization and lemmatization
lemmatizer = WordNetLemmatizer()
tokenized_product_names = product_names.apply(lambda x: word_tokenize(str(x)))  # Tokenization
lemmatized_product_names = tokenized_product_names.apply(lambda x: [lemmatizer.lemmatize(word) for word in x])  # Lemmatization

# Combine the lemmatized words back into strings
processed_product_names = lemmatized_product_names.apply(lambda x: ' '.join(x))

# Initialize the CountVectorizer
vectorizer = CountVectorizer()

# Fit and transform the processed product names
processed_product_name_features = vectorizer.fit_transform(processed_product_names)

# Convert the result to a DataFrame for better visualization
processed_feature_df = pd.DataFrame(processed_product_name_features.toarray(), columns=vectorizer.get_feature_names_out())

# Save the resulting DataFrame to a CSV file
output_file_path = "Text_Processing_Result.csv"
processed_feature_df.to_csv(output_file_path, index=False)

# Displaying the resulting DataFrame with processed features
print(processed_feature_df.head())
