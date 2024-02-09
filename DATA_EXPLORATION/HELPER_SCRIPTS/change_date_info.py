import pandas as pd

# Read the original CSV file
file_path = "Global_Superstore_Original.csv"
df = pd.read_csv(file_path)

# Convert 'Order Date' and 'Ship Date' to datetime objects
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Calculate the time difference in days and create a new 'Ship Time' column
df['Ship Time'] = (df['Ship Date'] - df['Order Date']).dt.days

# Drop 'Order Date' and 'Ship Date' columns
df = df.drop(columns=['Order Date', 'Ship Date'])

# Save the modified DataFrame to a new CSV file
new_file_path = "New_Global_Superstore.csv"
df.to_csv(new_file_path, index=False)

# Display the first few rows of the modified DataFrame
print(df.head())
