# -----------------------------
# Import NumPy
# -----------------------------
import numpy as np

# -----------------------------
# Python Lists
# -----------------------------
numbers_list = [1, 2, 3, 4, 5]
matrix_list = [[1, 2, 3], [4, 5, 6]]

# -----------------------------
# Convert Lists to NumPy Arrays
# -----------------------------
numbers_array = np.array(numbers_list)
matrix_array = np.array(matrix_list)

print("1D NumPy Array:")
print(numbers_array)

print("\n2D NumPy Array:")
print(matrix_array)

# -----------------------------
# Inspect Array Properties
# -----------------------------
print("\nArray Shape:", numbers_array.shape)
print("Array Data Type:", numbers_array.dtype)

print("\n2D Array Shape:", matrix_array.shape)
print("2D Array Data Type:", matrix_array.dtype)

# -----------------------------
# Basic Array Operations
# -----------------------------
print("\nAdding 10 to each element:")
print(numbers_array + 10)

print("\nMultiplying array by 2:")
print(numbers_array * 2)

# -----------------------------
# List vs Array Behavior
# -----------------------------
print("\nList * 2 (repeats elements):")
print(numbers_list * 2)

print("\nArray * 2 (element-wise multiplication):")
print(numbers_array * 2)