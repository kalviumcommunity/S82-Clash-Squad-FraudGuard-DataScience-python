# =========================
# IMPORTS
# =========================
import pandas as pd
import numpy as np


# =========================
# SERIES FROM PYTHON LIST
# =========================
def create_series_from_list():
    data_list = [10, 20, 30, 40]

    series_from_list = pd.Series(data_list)

    print("Series from Python List:")
    print(series_from_list)
    print("Index:", series_from_list.index)
    print("Values:", series_from_list.values)
    print()


# =========================
# SERIES FROM NUMPY ARRAY
# =========================
def create_series_from_array():
    numpy_array = np.array([100, 200, 300, 400])

    series_from_array = pd.Series(numpy_array)

    print("Series from NumPy Array:")
    print(series_from_array)
    print("Index:", series_from_array.index)
    print("Values:", series_from_array.values)
    print()


# =========================
# CUSTOM INDEX EXAMPLE
# =========================
def series_with_custom_index():
    data = [1, 2, 3]
    labels = ['a', 'b', 'c']

    custom_series = pd.Series(data, index=labels)

    print("Series with Custom Index:")
    print(custom_series)
    print("Access using label 'a':", custom_series['a'])
    print()


# =========================
# MAIN EXECUTION
# =========================
def main():
    create_series_from_list()
    create_series_from_array()
    series_with_custom_index()


if __name__ == "__main__":
    main()