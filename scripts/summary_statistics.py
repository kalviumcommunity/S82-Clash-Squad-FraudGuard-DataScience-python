import pandas as pd

# Step 1: Load dataset
df = pd.read_csv("data.csv")

# Step 2: Select a numeric column (replace with your column)
column1 = 'age'   # change if needed
column2 = 'salary'  # second column for comparison

print("----- Summary Statistics for Column 1 -----")
print(f"Column: {column1}")
print("Count:", df[column1].count())
print("Mean:", df[column1].mean())
print("Median:", df[column1].median())
print("Min:", df[column1].min())
print("Max:", df[column1].max())
print("Standard Deviation:", df[column1].std())

# Step 3: Compare with another column
print("\n----- Summary Statistics for Column 2 -----")
print(f"Column: {column2}")
print("Count:", df[column2].count())
print("Mean:", df[column2].mean())
print("Median:", df[column2].median())
print("Min:", df[column2].min())
print("Max:", df[column2].max())
print("Standard Deviation:", df[column2].std())