# Original Tuple
Tuple2 = ("Joseph", "Sam", 894.32, False, 2, 3, 2, 2, 2, 7)
print("Original Tuple2:", Tuple2)

# Accessing Elements (Indexing & Slicing)
print("First element:", Tuple2[0])
print("Last element:", Tuple2[-1])
print("Slice [1:5]:", Tuple2[1:5])

# Nested access example
nested = (1, [2, 3], (4, 5))
print("Nested tuple:", nested)
print("Nested list element:", nested[1][0])  # 2
print("Nested tuple element:", nested[2][1])  # 5

# Operations
tpl = (1, 2, 3)

# Concatenation
new_tpl = tpl + (4, 5)
print("Concatenation:", new_tpl)

# Repetition
print("Repetition:", tpl * 2)

# Membership
print("2 in tpl:", 2 in tpl)
print("9 not in tpl:", 9 not in tpl)

# Length
print("Length of tpl:", len(tpl))

# Tuple Methods (Limited)
tpl2 = (1, 2, 3, 2)

# index() → first occurrence of element
print("Index of 2:", tpl2.index(2))

# count() → number of occurrences
print("Count of 2:", tpl2.count(2))

# Conversion between List and Tuple
lst = [1, 2, 3]

# List → Tuple
tpl_from_list = tuple(lst)
print("Tuple from list:", tpl_from_list)

# Tuple → List
list_from_tpl = list(tpl_from_list)
print("List from tuple:", list_from_tpl)

# Tuple Comprehensions (Using Generators)
# Squares
tpl_squares = tuple(x**2 for x in range(5))
print("Squares:", tpl_squares)

# Even numbers
tpl_evens = tuple(x for x in range(10) if x % 2 == 0)
print("Evens:", tpl_evens)

# Nested tuple
tpl_nested = tuple(tuple(i * j for j in range(3)) for i in range(3))
print("Nested tuple:", tpl_nested)
