# Importing necessary libraries
import pandas as pd
import spacy

# Load spaCy's pre-trained word vectors model
nlp = spacy.load("en_core_web_md")

# Specify the file path to your "Global_Superstore.csv" file
file_path = "Drop_Columns.csv"

# Loading the dataset
df = pd.read_csv(file_path)

# Extracting features from the "Product Name" column
product_names = df['Product Name']

# Create a DataFrame to store the embeddings
embedding_list = []

# Iterate through each product name and get its vector representation
for product_name in product_names:
    doc = nlp(str(product_name))
    # Average the word vectors to get a single vector representation for the entire product name
    product_embedding = doc.vector
    embedding_list.append(product_embedding)

# Create a DataFrame from the list of embeddings
embedding_df = pd.DataFrame(embedding_list, columns=[f"embedding_{i}" for i in range(len(product_embedding))])

# Save the resulting DataFrame to a CSV file
output_file_path = "Word_Embeddings.csv"
embedding_df.to_csv(output_file_path, index=False)

# Displaying the resulting DataFrame with word embeddings
print(embedding_df.head())
