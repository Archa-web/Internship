# ---------------- LIST (list) DATA TYPE IN PYTHON ----------------- #

"""
NOTES:
- list is an ordered collection of elements.
- Lists are mutable (changeable).
- List allows duplicate values.
- List can store multiple data types
- List is written using square brackets []
"""

# Creating a list
numbers = [10, 20, 30, 40, 50]
fruits = ["apple", "banana", "cherry", "date"]
mixed_list = [10, "apple", 20.5, True, "banana",[1, 2, 3],(4, 5,"a"),{"key": "value","age": 25},{1,2,3}]

print(numbers)
print(fruits)
print(mixed_list)

# Check data type
print(type(numbers))      # <class 'list'>


#--------------- EMPTY LIST ----------------#

"""
Notes:
- Empty list means a list with no elements.
- Used when data will be added later dynamically.
"""

empty_list = []
print(empty_list)
print(type(empty_list))    # <class 'list'>


# ------------- LIST INDEXING -------------- #

"""
Notes:
- List is a sequence data type.
- List indexing starts from 0.
- Negative indexing starts from -1 (last element).
"""

sample_list = ["a", "b", "c", "d", "e"]

"""
a-> index 0, -5
b-> index 1, -4
c-> index 2, -3
d-> index 3, -2
e-> index 4, -1
"""

print(sample_list[0])    # a
print(sample_list[1])    # b
print(sample_list[4])    # e


# Negative Indexing
print(sample_list[-1])   # e
print(sample_list[-3])   # c

# ------------------LIST SLICING ------------------ #

"""
Notes:
- Slicing extracts a portion of the list.
Last index is NOT included in the slice.
- Syntax: list_name[start:end:step]
"""


print(sample_list[1:4])    # ['b', 'c', 'd']
print(sample_list[0:3])    # ['a', 'b', 'c']
print(sample_list[2:])     # ['c', 'd', 'e']
print(sample_list[:3])     # ['a', 'b', 'c']
print(sample_list[:])      # ['a', 'b', 'c', 'd', 'e'] # full list


print(sample_list[-4:-1])  # ['b', 'c', 'd']


# Step in Slicing
print(sample_list[0:5:2])   # ['a', 'c', 'e']
print(sample_list[::2])     # ['a', 'c', 'e']
print(sample_list[1::2])    # ['b', 'd']
print(sample_list[0:5:3])   # ['a', 'd']

# Negative Step  --> vvimp
print(sample_list[::-1])    # ['e', 'd', 'c', 'b', 'a']  # reverses the list
print(sample_list[::-2])   # ['e', 'c', 'a']
print(sample_list[4:1:-1])  # ['e', 'd', 'c']

