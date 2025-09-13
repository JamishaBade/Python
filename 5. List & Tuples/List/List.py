myList = [1, 4, 6, "Jamisha", "Bade", "7.32", True]
print(myList)

# Empty List
x = []
y = list()
z = [1, 2, 3]

d = list("hello")

t = (5,)
print(x, y, z, d, t)

# Indexing and Slicing
list = [10, 20, 30, 40, 50]
print(list[0])
print(list[-1])

# slicing
print(list[1:4])
print(list[:3])

# Nested access
nested = [1, [2, 3], (4, 5)]
print(nested)

# Lists are mutable
lst = [1, 2, 3]
lst[1] = 99
lst.append(100)
print(lst)

# Operations
lst = [1, 2, 3]
print(lst + [4, 5])  # Concatination
print(lst * 2)  # Repetition

# Membership
print(2 in lst)
print(9 not in lst)
print(100 in lst)

# Length
print(len(lst))

# List Methods

lst = [1, 2, 3, 2]

# Adding
lst.append(4)  # [1,2,3,2,4]
lst.insert(1, 10)  # [1,10,2,3,2,4]
lst.extend([5, 6])  # [1,10,2,3,2,4,5,6]

# Removing
lst.remove(2)  # removes first 2 → [1,10,3,2,4,5,6]
lst.pop()  # removes last → [1,10,3,2,4,5]
lst.pop(1)  # removes index 1 → [1,3,2,4,5]
del lst[2]  # delete index 2 → [1,3,4,5]

# Searching
print(lst.index(4))  # 2
print(lst.count(3))  # 1

# Sorting
print("Sorting")
lst.sort()  # in-place sort
lst.sort(reverse=True)  # descending
print(sorted(lst))  # returns new sorted list

# Utility
print("utility")
lst.reverse()
lst.clear()

# Conversion between tuple and list
lst = [1, 2, 3]
tpl = tuple(lst)  # (1, 2, 3)

new_lst = list(tpl)  # [1, 2, 3]

squares = [x**2 for x in range(5)]  # [0,1,4,9,16]
evens = [x for x in range(10) if x % 2 == 0]  # [0,2,4,6,8]
nested = [[i * j for j in range(3)] for i in range(3)]
