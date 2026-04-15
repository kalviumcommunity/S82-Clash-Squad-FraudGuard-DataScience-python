import pandas as pd

# Step 1: Load dataset
df = pd.read_csv("data.csv")

# Step 2: Show initial shape
print("Original Shape:", df.shape)


# -------------------------------
# 🔹 DETECT DUPLICATES
# -------------------------------

# Find duplicate rows (True = duplicate)
print("\n----- Duplicate Rows (Boolean) -----")
print(df.duplicated())

# Count number of duplicate rows
duplicate_count = df.duplicated().sum()
print("\nTotal Duplicate Rows:", duplicate_count)

# Show duplicate rows
print("\n----- Duplicate Records -----")
print(df[df.duplicated()])


# -------------------------------
# 🔹 REMOVE DUPLICATES
# -------------------------------

# Remove duplicates (keep first occurrence)
df_clean = df.drop_duplicates()

print("\n----- After Removing Duplicates -----")
print("New Shape:", df_clean.shape)


# -------------------------------
# 🔹 VERIFY RESULTS
# -------------------------------

# Check again for duplicates
print("\nRemaining Duplicates:", df_clean.duplicated().sum())