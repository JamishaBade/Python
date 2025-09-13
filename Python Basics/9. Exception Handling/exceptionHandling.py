# Try and Excpet
try:
    x = 10 / 0  # This will cause an exception
except ZeroDivisionError:
    print("Cannot divide by zero!")

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input! Not a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")


# Raising Exceptions
def check_age(age):
    if age < 18:
        raise ValueError("You must be at least 18!")
    print("Access granted")


check_age(15)
