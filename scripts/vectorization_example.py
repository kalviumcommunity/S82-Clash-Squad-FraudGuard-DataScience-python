import numpy as np

# -------------------------------
# 1. Create NumPy array
# -------------------------------
numbers = np.array([1, 2, 3, 4, 5])
print("Original Array:", numbers)


# -------------------------------
# 2. Loop-based approach
# -------------------------------
squared_loop = []

for num in numbers:
    squared_loop.append(num ** 2)

print("\nLoop-based result (squared):", squared_loop)


# -------------------------------
# 3. Vectorized approach
# -------------------------------
squared_vectorized = numbers ** 2

print("Vectorized result (squared):", squared_vectorized)


# -------------------------------
# 4. Verify both are same
# -------------------------------
print("\nAre results equal?",
      np.array_equal(np.array(squared_loop), squared_vectorized))


# -------------------------------
# 5. Vectorized comparison
# -------------------------------
greater_than_three = numbers > 3

print("\nVectorized Comparison (numbers > 3):")
print(greater_than_three)