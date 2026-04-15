# Function with parameters
def add_numbers(a, b):
    return a + b

# Function with parameters
def multiply_numbers(x, y):
    return x * y

# Calling function
sum_result = add_numbers(10, 5)
print("Sum:", sum_result)

# Using returned value again
final_result = multiply_numbers(sum_result, 2)
print("Final result:", final_result)