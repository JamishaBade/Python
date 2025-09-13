# Original Dictionary
dict1 = {"name": "Jamisha", "age": 16, "grade": 11, "city": "New York"}
print("Original Dictionary:", dict1)

# Accessing Elements

# Access value by key
print("Name:", dict1["name"])
print("Age:", dict1.get("age"))  # safer, returns None if key doesn't exist

# Access keys, values, items
print("Keys:", dict1.keys())
print("Values:", dict1.values())
print("Items:", dict1.items())

# Adding / Updating Elements

# Add a new key-value pair
dict1["school"] = "MCSM"
print("After adding school:", dict1)

# Update an existing key
dict1["age"] = 17
print("After updating age:", dict1)

# Using update() method
dict1.update({"grade": 12, "city": "NYC"})
print("After update():", dict1)

# Removing Elements
# pop() → remove key and return value
removed_value = dict1.pop("city")
print("After pop('city'):", dict1)
print("Removed value:", removed_value)

# popitem() → removes last inserted key-value pair (Python 3.7+)
last_item = dict1.popitem()
print("After popitem():", dict1)
print("Last removed item:", last_item)

# del → remove key
# vdel dict1["school"]
# print("After del 'school':", dict1)

# clear() → remove all items
dict1.clear()
print("After clear():", dict1)

# Checking Membership
dict2 = {"a": 1, "b": 2, "c": 3}
print("'a' in dict2:", "a" in dict2)
print("'z' not in dict2:", "z" not in dict2)

# Copying / Conversion

# copy() → shallow copy
copy_dict = dict2.copy()
print("Copy:", copy_dict)

# dict() constructor → create new dictionary
new_dict = dict(a=10, b=20)
print("New dictionary:", new_dict)

# From list of tuples → convert to dict
lst_of_tuples = [("x", 100), ("y", 200)]
dict_from_list = dict(lst_of_tuples)
print("Dictionary from list of tuples:", dict_from_list)

# Iterating Through Dictionary
for key in dict2:
    print("Key:", key, "Value:", dict2[key])

# Using items() to get key-value pairs
for k, v in dict2.items():
    print(f"Key: {k}, Value: {v}")


# Dictionary Comprehensions


# Square numbers
squares = {x: x**2 for x in range(5)}
print("Squares dictionary:", squares)

# Conditional comprehension (even numbers only)
evens = {x: x**2 for x in range(10) if x % 2 == 0}
print("Even squares dictionary:", evens)
