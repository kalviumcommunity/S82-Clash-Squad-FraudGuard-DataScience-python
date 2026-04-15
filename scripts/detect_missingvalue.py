import pandas as pd

# Step 1: Load dataset
df = pd.read_csv("data.csv")

# Step 2: Detect missing values (True = missing)
print("----- Missing Values (Boolean Mask) -----")
print(df.isnull())

# Step 3: Count missing values per column
print("\n----- Missing Values Count Per Column -----")
print(df.isnull().sum())

# Step 4: Total missing values in dataset
print("\n----- Total Missing Values -----")
print(df.isnull().sum().sum())

# Step 5: Show rows with missing values
print("\n----- Rows with Missing Values -----")
print(df[df.isnull().any(axis=1)])