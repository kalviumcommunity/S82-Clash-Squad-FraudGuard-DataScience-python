# Numeric Data Types

# Integer
a = 10
b = 5

# Float
c = 2.5

# Arithmetic operations
print("Addition:", a + b)
print("Division:", a / b)
print("Multiplication:", b * c)

print("\n--- String Data Types ---")

# String variables
name = "John"
message = "Hello"

# String concatenation
print(message + " " + name)

# String formatting
print(f"Welcome {name}")

print("\n--- Type Checking ---")

# Check types
print(type(a))
print(type(c))
print(type(name))

print("\n--- Mixing Types ---")

# Wrong way (will cause error if uncommented)
# print("Total: " + a)

# Correct way using conversion
print("Total:", str(a))

# Convert string to number
num_str = "100"
num_int = int(num_str)
print("Converted to int:", num_int + 50)