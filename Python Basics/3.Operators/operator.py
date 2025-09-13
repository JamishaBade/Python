# Arithmetic
x = 10
y = 20
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)  # floor division  (no decimal)
print(x % y)
print(x**2)  # exponential


# Comparision
print(x == y)
print(x != y)
print(x >= y)
print(x <= y)
print(x < y)

# LOGICAL
age = 18
is_student = True
print("logical operator:")
print(age > 10 and is_student)
print(age > 90 or is_student)

# IDENTITY OPERATORS
x = [1, 2, 3]
y = x  # y points to the same object as x
z = [1, 2, 3]  # z is a different object with the same values

print(x is y)  # True  (same memory location)
print(x is z)  # False (different objects, even though values are equal)
print(x == z)  # True  (values are equal, but objects are different)
print(x is not z)  # True

# Membership Operators
nums = [10, 20, 30, 40]
print(20 in nums)  # True  (20 is in the list)
print(25 in nums)  # False
print(50 not in nums)  # True  (50 is not in the list)

text = "hello world"
print("hello" in text)  # True
print("bye" not in text)  # True
