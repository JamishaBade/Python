a = "Hello World"  # upper()
print(a.upper())

b = "HELLO WORLD"
print(b.lower())

# removing whitespaces

a = "Hello, world   "
print(a)
print(a.strip())


# replace strings

a = "Mathematics"
print(a.replace("M", "J"))


a = "Mountains"
print("id of a:", id(a))
# strings are immutable and here while replacing a new string is created always
b = a.replace("M", "J")
print("id of b:", id(b))

print("a =", a)
print("b =", b)
