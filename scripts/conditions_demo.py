# -------- BASIC IF --------
age = 18

if age >= 18:
    print("You are eligible to vote")


# -------- IF-ELSE --------
temperature = 30

if temperature > 25:
    print("It's hot outside")
else:
    print("It's not hot")


# -------- IF-ELIF-ELSE --------
marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
else:
    print("Grade: C")


# -------- LOGICAL OPERATORS --------
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Login failed")


# -------- USING OR --------
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("It's weekend")
else:
    print("It's weekday")


# -------- USING NOT --------
is_logged_in = False

if not is_logged_in:
    print("User is not logged in")