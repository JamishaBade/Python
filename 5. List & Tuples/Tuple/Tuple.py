# Creating tuples
myTuple = (1, 4, 6, "Jamisha", "Bade", "7.32", True)
print(myTuple)

# Empty tuple
x = ()
y = tuple()
z = (1, 2, 3)

# Single element tuple (comma needed!)
t = (5,)
print(x, y, z, t)

# Indexing and Slicing
tpl = (10, 20, 30, 40, 50)
print(tpl[0])  # first element
print(tpl[-1])  # last element

# Slicing
print(tpl[1:4])  # (20, 30, 40)
print(tpl[:3])  # (10, 20, 30)

# Nested access
nested = (1, [2, 3], (4, 5))
print(nested)
print(nested[1][0])  # 2
print(nested[2][1])  # 5

# Tuples are immutable
tpl = (1, 2, 3)
# tpl[1] = 99  # this will give error
# tpl.append(4)

# Operations
tpl = (1, 2, 3)
print(tpl + (4, 5))  # Concatenation
print(tpl * 2)  # Repetition

# Membership
print(2 in tpl)
print(9 not in tpl)
print(100 in tpl)

# Length
print(len(tpl))

# Tuple methods (limited)
tpl = (1, 2, 3, 2)
print(tpl.count(2))  # 2 occurrences of 2
print(tpl.index(3))  # index of 3 -> 2

# Conversion between list and tuple
lst = [1, 2, 3]
tpl = tuple(lst)  # (1, 2, 3)
new_lst = list(tpl)  # [1, 2, 3]

# Comprehensions (tuples can't have list comprehensions directly)
tpl_squares = tuple(x**2 for x in range(5))  # (0,1,4,9,16)
tpl_evens = tuple(x for x in range(10) if x % 2 == 0)  # (0,2,4,6,8)
tpl_nested = tuple(tuple(i * j for j in range(3)) for i in range(3))
# ((0,0,0),(0,1,2),(0,2,4))

print(tpl_squares)
print(tpl_evens)
print(tpl_nested)
