# Bad variable naming (for demonstration)
x = 10
y = 5
z = x + y
print("Bad naming result:", z)

# Good variable naming (PEP8 style)
first_number = 10
second_number = 5
sum_of_numbers = first_number + second_number
print("Good naming result:", sum_of_numbers)

# Function with clear naming
def calculate_total_price(price, tax):
    # Adding tax to price to get final amount
    total_price = price + tax
    return total_price

# Calling function
final_amount = calculate_total_price(100, 18)
print("Final amount:", final_amount)

# Example showing why comments matter
# We apply discount before tax calculation for correct pricing
discount = 10
price_after_discount = final_amount - discount
print("Price after discount:", price_after_discount)