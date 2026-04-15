# -------- FOR LOOP (range) --------
print("For loop with range:")
for i in range(5):
    print("Number:", i)


# -------- FOR LOOP (list) --------
print("\nFor loop with list:")
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print("Fruit:", fruit)


# -------- WHILE LOOP --------
print("\nWhile loop:")
count = 0

while count < 5:
    print("Count:", count)
    count += 1   # IMPORTANT (prevents infinite loop)


# -------- BREAK --------
print("\nUsing break:")
for i in range(10):
    if i == 5:
        print("Breaking at:", i)
        break
    print(i)


# -------- CONTINUE --------
print("\nUsing continue:")
for i in range(5):
    if i == 2:
        continue
    print(i)