# -------- FUNCTION DEFINITION --------
def greet(name):
    print("Hello,", name)


# -------- FUNCTION WITH PARAMETERS --------
def add_numbers(a, b):
    result = a + b
    print("Sum:", result)


# -------- FUNCTION WITH RETURN --------
def multiply(x, y):
    return x * y


# -------- FUNCTION CALLS --------
greet("John")

add_numbers(5, 10)

product = multiply(4, 3)
print("Product:", product)


# -------- FUNCTION SCOPE --------
def show_value():
    value = 100   # local variable
    print("Inside function:", value)

show_value()

# print(value)  # This will cause error (outside scope)