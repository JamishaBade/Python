a = 10
b = 20
print(a + b)

a = 30
b = 40
print(a + b)

# resuability
# modularity
# scoping


def greet():
    print("hi")


def greetings(name):
    print("Hello ", name)


def city(name, country):
    print(f"welcome to {name}, {country}")


greet()
greetings("Jamisha")
greetings("Sambhav")
greetings("Shreya")
city("NYC", "United States")


def greet(name="Friend"):
    print(f"Hello, {name}!")


greet()  # Hello, Friend!
greet("Jamisha")  # Hello, Jamisha!
