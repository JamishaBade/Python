def decorator(func):
    def wrapper():
        print("Something before the function runs...")
        func()
        print("Something after the function runs...")

    return wrapper


@decorator
def say_hello():
    print("Hello!")


say_hello()
# A decorator in Python is just a function that takes another function as input, adds some extra functionality to it, and then returns it.

import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args)  # run the original function
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result

    return wrapper


@timer
def compute():
    sum(
        [i**2 for i in range(100000000)]
    )  # the larger the seconds the larger our num will be because it will take longer to compute


compute()
