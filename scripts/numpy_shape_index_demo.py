# -----------------------------
# Import NumPy
# -----------------------------
import numpy as np

# -----------------------------
# Create Arrays
# -----------------------------

# 1D Array
one_d_array = np.array([10, 20, 30, 40])

# 2D Array
two_d_array = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("1D Array:")
print(one_d_array)

print("\n2D Array:")
print(two_d_array)

# -----------------------------
# Shape and Dimensions
# -----------------------------
print("\n1D Shape:", one_d_array.shape)
print("1D Dimensions:", one_d_array.ndim)

print("\n2D Shape:", two_d_array.shape)
print("2D Dimensions:", two_d_array.ndim)

# -----------------------------
# Accessing Elements (Indexing)
# -----------------------------

# 1D indexing
print("\n1D Array Element at index 2:", one_d_array[2])

# 2D indexing (row, column)
print("2D Element at row 0, column 1:", two_d_array[0][1])
print("2D Element at row 1, column 2:", two_d_array[1][2])

# -----------------------------
# Visual Understanding
# -----------------------------
print("\nExplanation:")
print("2D array shape (2,3) means 2 rows and 3 columns")
print("Indexing starts from 0 (zero-based indexing)")