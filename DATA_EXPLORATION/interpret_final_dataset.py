import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Final_Dataset.csv')

# 1. Descriptive Statistics
print("Summary Statistics:")
print(df.describe())

# 2. Correlation Analysis
correlation_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

# 3. Category-wise Analysis
category_analysis = df.groupby('Category_encoded').agg({'Sales': 'mean', 'Profit': 'mean'})
print("Category-wise Analysis:")
print(category_analysis)

# 4. Discount Analysis
discount_analysis = df.groupby('Discount').agg({'Sales': 'mean', 'Profit': 'mean'})
print("Discount Analysis:")
print(discount_analysis)

# 5. Shipping Cost and Profit Analysis
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Shipping Cost', y='Profit', data=df)
plt.title("Shipping Cost vs Profit")
plt.show()

# 6. Order Priority Analysis
order_priority_analysis = df.groupby('Order Priority').agg({'Sales': 'mean', 'Profit': 'mean'})
print("Order Priority Analysis:")
print(order_priority_analysis)

# 7. Segment-wise Analysis
segment_analysis = df.groupby('Segment_encoded').agg({'Sales': 'mean', 'Profit': 'mean'})
print("Segment-wise Analysis:")
print(segment_analysis)

# 8. Visualization
plt.figure(figsize=(12, 6))
sns.histplot(df['Sales'], kde=True, bins=30)
plt.title("Distribution of Sales")
plt.show()

# Show all plots
plt.show()
