import pandas as pd

# Step 1: Load CSV file (make sure file is in same folder)
df = pd.read_csv("data.csv")

# Step 2: Preview data using head()
print("----- First 5 Rows -----")
print(df.head())

# Step 3: Inspect structure using info()
print("\n----- DataFrame Info -----")
print(df.info())

# Step 4: Describe numeric data
print("\n----- Statistical Summary -----")
print(df.describe())