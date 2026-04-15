import numpy as np

# -------------------------------
# 1. Creating NumPy arrays
# -------------------------------
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])

print("Array A:", array_a)
print("Array B:", array_b)


# -------------------------------
# 2. Element-wise operations
# -------------------------------
addition_result = array_a + array_b
subtraction_result = array_a - array_b
multiplication_result = array_a * array_b
division_result = array_a / array_b

print("\nElement-wise Operations:")
print("Addition:", addition_result)
print("Subtraction:", subtraction_result)
print("Multiplication:", multiplication_result)
print("Division:", division_result)


# -------------------------------
# 3. Scalar operations
# -------------------------------
scalar_add = array_a + 10
scalar_multiply = array_b * 2

print("\nScalar Operations:")
print("Array A + 10:", scalar_add)
print("Array B * 2:", scalar_multiply)


# -------------------------------
# 4. Shape check (important)
# -------------------------------
print("\nArray Shapes:")
print("Shape of A:", array_a.shape)
print("Shape of B:", array_b.shape)