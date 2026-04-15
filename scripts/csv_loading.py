# =========================
# IMPORTS
# =========================
import pandas as pd


# =========================
# LOAD CSV FILE
# =========================
def load_csv_file():
    # Make sure the CSV file is in the same folder
    df = pd.read_csv("students.csv")

    print("CSV Loaded Successfully!\n")

    # Preview first few rows
    print("First 5 Rows:")
    print(df.head())
    print()

    # Column names
    print("Columns:")
    print(df.columns)
    print()

    # Shape (rows, columns)
    print("Shape:")
    print(df.shape)
    print()

    # Data types
    print("Data Types:")
    print(df.dtypes)
    print()


# =========================
# MAIN FUNCTION
# =========================
def main():
    load_csv_file()


if __name__ == "__main__":
    main()