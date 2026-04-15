import pandas as pd

# Step 1: Load dataset
df = pd.read_csv("data.csv")

# Step 2: Check missing values BEFORE handling
print("----- Missing Values Before -----")
print(df.isnull().sum())

print("\nShape Before:", df.shape)


# -------------------------------
# 🔹 DROP STRATEGY
# -------------------------------

# Drop rows with missing values
df_drop_rows = df.dropna()

print("\n----- After Dropping Rows -----")
print(df_drop_rows.isnull().sum())
print("Shape After Dropping Rows:", df_drop_rows.shape)


# Drop columns with missing values
df_drop_cols = df.dropna(axis=1)

print("\n----- After Dropping Columns -----")
print(df_drop_cols.isnull().sum())
print("Shape After Dropping Columns:", df_drop_cols.shape)


# -------------------------------
# 🔹 FILL STRATEGY
# -------------------------------

# Fill with constant value
df_fill_const = df.fillna(0)

print("\n----- After Filling with Constant (0) -----")
print(df_fill_const.isnull().sum())


# Fill numeric columns with mean
df_fill_mean = df.copy()
for col in df_fill_mean.select_dtypes(include='number').columns:
    df_fill_mean[col] = df_fill_mean[col].fillna(df_fill_mean[col].mean())

print("\n----- After Filling with Mean -----")
print(df_fill_mean.isnull().sum())


# Fill categorical columns with mode
df_fill_mode = df.copy()
for col in df_fill_mode.select_dtypes(include='object').columns:
    df_fill_mode[col] = df_fill_mode[col].fillna(df_fill_mode[col].mode()[0])

print("\n----- After Filling with Mode -----")
print(df_fill_mode.isnull().sum())


# Final shape comparison
print("\nOriginal Shape:", df.shape)
print("After Drop Rows:", df_drop_rows.shape)
print("After Drop Columns:", df_drop_cols.shape)