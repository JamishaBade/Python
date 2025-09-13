# Original List
List2 = ["Joseph", "Sam", 894.32, False, 2, 3, 2, 2, 2, 7]
print("Original List2:", List2)

# Adding Elements

# append() → add one element at the end
List2.append("Bade")
print("After append:", List2)

# insert() → insert element at specific index
List2.insert(1, "Inserted")
print("After insert:", List2)

# extend() → add multiple elements from an iterable
List2.extend([10, 20, 30])
print("After extend:", List2)

# Removing Elements

# remove() → remove first occurrence of element
List2.remove(2)
print("After remove(2):", List2)

# pop() → remove element at index (default last)
removed_element = List2.pop(3)
print("After pop(3):", List2)
print("Removed element:", removed_element)

# del → delete element by index
del List2[0]
print("After del index 0:", List2)

# clear() → remove all elements
List2.clear()
print("After clear():", List2)

# Searching & Counting
List2 = ["Joseph", "Sam", 894.32, False, 2, 3, 2, 2, 2, 7]

# index() → first occurrence of element
print("Index of 2:", List2.index(2))

# count() → number of occurrences of element
print("Count of 2:", List2.count(2))

# Sorting & Reversing
num_list = [5, 2, 9, 1, 7]

# sort() → in-place ascending
num_list.sort()
print("Sorted list:", num_list)

# sort() with reverse=True → descending
num_list.sort(reverse=True)
print("Descending sort:", num_list)

# sorted() → returns new sorted list, original not changed
original_list = [5, 2, 9, 1, 7]
new_sorted = sorted(original_list)
print("Original list:", original_list)
print("New sorted list:", new_sorted)

# reverse() → reverse the list in-place
num_list.reverse()
print("Reversed list:", num_list)

# Copying Lists
copy_list = List2.copy()
print("Copy of List2:", copy_list)

# Shallow copy using list()
another_copy = list(List2)
print("Another copy:", another_copy)

# Length, Max, Min, Sum
numbers = [1, 4, 7, 2, 9]

print("Length:", len(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))

# List Comprehensions
# Squares
squares = [x**2 for x in range(5)]
print("Squares:", squares)

# Even numbers
evens = [x for x in range(10) if x % 2 == 0]
print("Evens:", evens)

# Nested list
nested = [[i * j for j in range(3)] for i in range(3)]
print("Nested list:", nested)
