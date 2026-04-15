import pandas as pd

# Step 1: Load CSV file
df = pd.read_csv("data.csv")

# Step 2: Check shape
print("----- DataFrame Shape -----")
print(df.shape)

# Step 3: Explain rows & columns
print("\nNumber of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

# Step 4: Check column data types
print("\n----- Column Data Types -----")
print(df.dtypes)