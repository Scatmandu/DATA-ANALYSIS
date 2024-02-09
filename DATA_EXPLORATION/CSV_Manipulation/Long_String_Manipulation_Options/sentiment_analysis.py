import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

# Load the original CSV
df = pd.read_csv("Drop_Columns.csv")

# Extract product names for sentiment analysis
product_names = df['Product Name']

# Initialize the Sentiment Intensity Analyzer
sia = SentimentIntensityAnalyzer()

# Perform sentiment analysis on each product name
sentiments = product_names.apply(lambda x: sia.polarity_scores(x)['compound'])

# Create a new column 'Sentiment' in the DataFrame
df['Sentiment'] = sentiments

# Save the DataFrame with sentiment scores to a new CSV file
df.to_csv("Sentiment_Analyzed.csv", index=False)
