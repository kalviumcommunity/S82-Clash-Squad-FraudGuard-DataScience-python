# LIST EXAMPLE
print("----- LIST -----")
fruits = ["apple", "banana", "cherry"]

# Access
print("First fruit:", fruits[0])

# Modify
fruits[1] = "orange"

# Add
fruits.append("grape")

print("Updated list:", fruits)


# TUPLE EXAMPLE
print("\n----- TUPLE -----")
colors = ("red", "green", "blue")

# Access
print("First color:", colors[0])

# Immutability test
try:
    colors[1] = "yellow"
except TypeError as e:
    print("Tuple cannot be changed:", e)


# DICTIONARY EXAMPLE
print("\n----- DICTIONARY -----")
student = {
    "name": "John",
    "age": 20,
    "course": "Data Science"
}

# Access
print("Student name:", student["name"])

# Modify
student["age"] = 21

# Add new key
student["grade"] = "A"

print("Updated dictionary:", student)