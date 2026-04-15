import pandas as pd

# Step 1: Load dataset
df = pd.read_csv("data.csv")

# Step 2: Select numeric columns (change based on your dataset)
columns = ['age', 'salary', 'experience']  # modify if needed

# Step 3: Compute summary statistics for selected columns
print("----- Summary Statistics for Selected Columns -----")
print(df[columns].describe())

# Step 4: Compare central tendency (mean & median)
print("\n----- Central Tendency Comparison -----")
for col in columns:
    print(f"\nColumn: {col}")
    print("Mean:", df[col].mean())
    print("Median:", df[col].median())

# Step 5: Compare spread (range & standard deviation)
print("\n----- Spread & Variability Comparison -----")
for col in columns:
    print(f"\nColumn: {col}")
    print("Min:", df[col].min())
    print("Max:", df[col].max())
    print("Range:", df[col].max() - df[col].min())
    print("Standard Deviation:", df[col].std())