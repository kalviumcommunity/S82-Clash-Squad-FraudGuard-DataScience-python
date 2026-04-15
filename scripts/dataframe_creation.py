# =========================
# IMPORTS
# =========================
import pandas as pd


# =========================
# DATAFRAME FROM DICTIONARY
# =========================
def create_dataframe_from_dict():
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [20, 21, 22],
        "Marks": [85, 90, 88]
    }

    df = pd.DataFrame(data)

    print("DataFrame from Dictionary:")
    print(df)
    print("Columns:", df.columns)
    print("Shape:", df.shape)
    print()


# =========================
# DATAFRAME FROM CSV FILE
# =========================
def load_dataframe_from_csv():
    # Make sure this file exists in your folder
    df = pd.read_csv("sample_data.csv")

    print("DataFrame from CSV:")
    print(df.head())  # first 5 rows
    print("Columns:", df.columns)
    print("Shape:", df.shape)
    print("Data Types:\n", df.dtypes)
    print()


# =========================
# MAIN FUNCTION
# =========================
def main():
    create_dataframe_from_dict()
    load_dataframe_from_csv()


if __name__ == "__main__":
    main()