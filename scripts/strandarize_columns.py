import pandas as pd

# Step 1: Load dataset
df = pd.read_csv("data.csv")

# Step 2: Show original column names
print("----- Original Columns -----")
print(df.columns)

# Step 3: Standardize column names
df.columns = (
    df.columns
    .str.lower()              # convert to lowercase
    .str.strip()              # remove leading/trailing spaces
    .str.replace(" ", "_")    # replace spaces with underscore
    .str.replace(r"[^\w_]", "", regex=True)  # remove special characters
)

print("\n----- Standardized Columns -----")
print(df.columns)

# Step 4: Standardize text column (example)
# Replace 'name' with any column in your dataset
if 'name' in df.columns:
    df['name'] = df['name'].str.lower().str.strip()

# Step 5: Convert numeric column (if stored as string)
# Replace 'age' with your column
if 'age' in df.columns:
    df['age'] = pd.to_numeric(df['age'], errors='coerce')

# Step 6: Convert date column (if exists)
# Replace 'date' with your column
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Step 7: Show updated dataset preview
print("\n----- Cleaned Data Preview -----")
print(df.head())