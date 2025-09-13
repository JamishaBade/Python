def sum_all(*numbers):  # args (elements to tupe)
    total = 0
    for n in numbers:
        total += n
    return total


print(sum_all(1, 2, 3, 4))  # 10
lists = [1, 2, 3, 4]
print(sum_all(*lists))


def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")


print_info(name="Jamisha", age=16, city="NY")


# Lambda function
# A lambda function is a small, anonymous function defined with the keyword lambda
square = lambda x: x**2
print(square(5))  # 25

# Lambda with multiple arguments
add = lambda a, b: a + b
print(add(3, 7))  # 10


numbers = [1, 2, 3, 4, 5]

# map() → apply a function to all elements
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1,4,9,16,25]

# filter() → select elements based on a condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2,4]

# reduce() → cumulative operation (needs functools)
from functools import reduce

sum_all = reduce(lambda a, b: a + b, numbers)
print(sum_all)  # 15


def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()


outer()


def greet(name):
    """This function greets a person by name."""
    print(f"Hello, {name}!")


print(greet.__doc__)


x = 10  # Global variable


def func():
    y = 5  # Local variable
    print("Inside:", x, y)


func()
print("Outside:", x)
# print(y)


def modify_global():
    global x
    x = 20


modify_global()
print(x)  # 20


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))  # 120


def greet(name):
    """This function greets a person by name."""
    print(f"Hello, {name}!")


print(greet.__doc__)

x = 10  # Global variable


def func():
    y = 5  # Local variable
    print("Inside:", x, y)


func()
print("Outside:", x)
# print(y)  # Error: y is local to func


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))  # 120
