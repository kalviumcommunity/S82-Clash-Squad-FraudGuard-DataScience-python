import pandas as pd

# Load CSV
df = pd.read_csv("data.csv")

print("----- Original Data -----")
print(df)

# 1. Select single column
print("\n----- Single Column (Name) -----")
print(df["Name"])

# 2. Select multiple columns
print("\n----- Multiple Columns (Name, Marks) -----")
print(df[["Name", "Marks"]])

# 3. Select rows by position (iloc)
print("\n----- Row by Position (index 0) -----")
print(df.iloc[0])

# 4. Slice rows by position
print("\n----- Rows 0 to 2 -----")
print(df.iloc[0:3])

# 5. Select rows by label (loc)
print("\n----- Row by Label (index 1) -----")
print(df.loc[1])

# 6. Slice rows by label
print("\n----- Rows 1 to 3 (label-based) -----")
print(df.loc[1:3])

# 7. Select rows and columns together
print("\n----- Rows 0 to 2 and Columns Name, Marks -----")
print(df.loc[0:2, ["Name", "Marks"]])