# Null
result = None
print(result)

# Sequence (String, List, tuple)

# String
name = "Jamisha"  # sequence of characters, immutable (cannot be changed)
Text = "This is a sentence"

# List (mutable)
my_list = ["data", "data2", "data3"]

# Tuple (immutable)
my_tuple = ("data1", "data2", "data3")


# Numeric type
"""
int - whole number (negative, postive and zero)
float - decimal numbers
complex number - real and imaginary part
a+bj
"""
int = 10
float = 10.32
complex = 3 + 4j
print(int, float, complex)

# logical operators (True/False)
is_raining = True
is_lockingIn = True
is_sunny = False
print(is_raining, is_lockingIn, is_sunny)

# Set type
my_set = {1, 2, 3, 3, 4, 4, 4, 5}
my_set.add(10)
print(my_set)  # {1, 2, 3, 4}

# Frozen type (immutable)

immutable_set = frozenset([1, 2, 3, 3, 3, 4, 5, 6])
# Error : immutable_set.add(20)
print(immutable_set)


#  Mapping Data Types

# Empty dictionary
my_dict = {}

# Dictionary with key-value pairs
my_dict = {"name": "Jamisha", "age": 16, "city": "NYC"}

# Using dict() constructor
my_dict2 = dict(name="Bade", age=10)

print(my_dict["name"])  # Alice

# Using get() to avoid KeyError
print(my_dict.get("country", "Unknown"))  # Unknown

my_dict["age"] = 26  # Update
my_dict["country"] = "USA"  # Add new
del my_dict["city"]  # Remove key-value pair
value = my_dict.pop("age")  # Remove and return value
