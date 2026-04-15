import numpy as np

# -------------------------------
# 1. Scalar to array broadcasting
# -------------------------------
array_1d = np.array([1, 2, 3])

print("Original 1D Array:", array_1d)
print("Shape:", array_1d.shape)

scalar_result = array_1d + 10

print("\nAfter adding scalar (10):", scalar_result)


# -------------------------------
# 2. 1D to 2D broadcasting
# -------------------------------
array_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

array_1d_broadcast = np.array([10, 20, 30])

print("\n2D Array:\n", array_2d)
print("Shape:", array_2d.shape)

print("\n1D Array:", array_1d_broadcast)
print("Shape:", array_1d_broadcast.shape)

# Broadcasting happens here
broadcast_result = array_2d + array_1d_broadcast

print("\nBroadcasted Result:\n", broadcast_result)


# -------------------------------
# 3. Shape reasoning
# -------------------------------
print("\nExplanation:")
print("2D shape:", array_2d.shape)
print("1D shape:", array_1d_broadcast.shape)
print("NumPy aligns from right → (2,3) and (3,) → compatible")