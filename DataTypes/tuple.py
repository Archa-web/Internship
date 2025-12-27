

# ----------- TUPLE (tuple) DATA TYPE IN PYTHON -------------- #

"""
NOTES:
- tuple is an ordered collection of elements.
- Tuples are immutable (unchangeable).
- Tuple allows duplicate values.
- Tuple can store multiple data types
- Tuple is written using parentheses ()
- Tuples are generally faster than lists.
- Tuple uses less memory than lists.
- Tuples can be used as dictionary keys (list cannot).
"""

# Creating a tuple
numbers = (10, 20, 30, 40, 50)
fruits = ("apple", "banana", "cherry", "date")
mixed_tuple = (10, "apple", 20.5, True, "banana",(1, 2, 3),["a", "b"],{"key": "value","age": 25},{1,2,3})

print(numbers)
print(fruits)
print(mixed_tuple)

# Check data type
print(type(numbers))      # <class 'tuple'>






# --------------- SINGLE ELEMENT TUPLE VVIMP --------------- #

"""
Notes:
- To create a single element tuple, a comma is required after the element.
- Without the comma, it is treated as a regular parenthesis.
"""

# correct single element tuple
single_tuple = (5,)
print(single_tuple)          # (5,)
print(type(single_tuple))    # <class 'tuple'>


# incorrect single element tuple (not a tuple)
not_a_tuple = (5)
print(not_a_tuple)          # 5
print(type(not_a_tuple))    # <class 'int'>


# Single element with tailing comma
single_tuple2 = ("Hello",)
print(single_tuple2)          # ('Hello',)
print(type(single_tuple2))    # <class 'tuple'>





# --------------- TUPLE WITHOUT PARENTHESIS --------------- #

"""
Notes:
- Tuples can create without using parentheses.
- Comma makes it a tuple, not parantheses.
- paratheses are optional in tuple creation, but recommended for clarity.
"""

# creating tuple without parentheses
tuple_without_parentheses = 1, 2, 3, 4, 5
print(tuple_without_parentheses)   # (1, 2, 3, 4, 5)
print(type(tuple_without_parentheses))  # <class 'tuple'>

# Single element tuple without parentheses
single_packed = 5,
print(single_packed)          # (5,)
print(type(single_packed))    # <class 'tuple'>





# --------------- EMPTY TUPLE --------------- #
"""
Notes:
- Empty tuple means a tuple with no elements.
- Less common than empty lists since tuples are immutable.
"""

empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))    # <class 'tuple'>
print(len(empty_tuple))     # 0





# ------------- TUPLE INDEXING -------------- #

"""
Notes:
- Tuple is a sequence data type.
- Tuple indexing starts from 0.
- Negative indexing starts from -1 (last element).
"""

sample_tuple = ("a", "b", "c", "d", "e")
print(sample_tuple[0])    # a
print(sample_tuple[1])    # b
print(sample_tuple[4])    # e

# Negative Indexing
print(sample_tuple[-1])   # e
print(sample_tuple[-3])   # c

# Index out of the range
# print(sample_tuple[5])    # IndexError
# print(sample_tuple[-6])   # IndexError





# ----------------- LENGTH OF TUPLE ----------------- #

"""
Notes:
- len() returns the number of elements in the tuple.
- Counts all elements including duplicates.
"""

my_tuple = (10, 20, 30, 40, 50, 20)
print("Length of tuple = ",len(my_tuple))    # 6

duplicate_tuple = (1, 2, 2, 3, 4, 4, 4)
print("Length of duplicate tuple = ",len(duplicate_tuple))    # 7





# ----------------- TUPLE SLICING ----------------- #

"""
Notes:
- Slicing extracts a portion of the tuple.
- Returns a NEW tuple.
- Last index is not included.
- Syntax: tuple_name[start_index:end_index:step]
- Original tuple remains unchanged.
"""


new_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90)
print(new_tuple[2:5])    # (30, 40, 50)
print(new_tuple[0:3])    # (10, 20, 30)
print(new_tuple[3:])     # (40, 50, 60, 70, 80, 90)
print(new_tuple[:4])     # (10, 20, 30, 40)
print(new_tuple[:])      # (10, 20, 30, 40, 50, 60, 70, 80, 90) # full tuple


# Negative Slicing

print(new_tuple[-5:-2])  # (50, 60, 70)

# Reversed tuple using slicing
print(new_tuple[::-1])    # (90, 80, 70, 60, 50, 40, 30, 20, 10)
print(new_tuple[7:4:-1]) # (80, 70, 60)





# ---------------- TUPLE IS IMMUTABLE ---------------- #

"""
Notes:
- Cannot modify, add, or remove elements from a tuple after creation.
- Cannot change elements values.
- Attempting to do so will raise a TypeError.
- This is the KEY difference between list and tuple.
- Immutability makes tuple faster and more memory efficient.
- Immutability allows tuple to be used as dictionary keys.
"""

# Trying to change an element (will raise error)
immutable_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", immutable_tuple)

# cannot modify element
# immutable_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment
print("Cannot modify elements of tuple")





# ---------------- TUPLE WITH MUTABLE ELEMENTS VVIMP ---------------- #

"""
Notes:
- Tuple itself is immutable.
- But if a tuple contains mutable elements (like lists), those elements can be modified.
"""

tuple_with_list = (1, 2, [3, 4])
print("Before modification:", tuple_with_list)  # (1, 2, [3, 4])

# Cannot modify elements of tuple
# tuple_with_list[0] = 10  # TypeError: 'tuple' object does not support item assignment

# using append will add the element at the end.

tuple_with_list[2].append(5)
print("After modification:", tuple_with_list)   # (1, 2, [3, 4, 5])


# Modifying the mutable element (list) inside the tuple
tuple_with_list[2][1] = 30
print("After modification:", tuple_with_list)   # (1, 2, [30, 4, 5])






# -------------------- TUPLE CONCATENATION ------------------- #

"""
Notes:
- Can combine tuples using + operator.
- Creates a NEW tuple.
- Original tuples remain unchanged.
- Cannot use += on tuple variable (creates new tuple)
"""

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print("Tuple 1:", tuple1)   # (1, 2, 3)
print("Tuple 2:", tuple2)   # (4, 5, 6)
print("Concatenated Tuple:", tuple1 + tuple2)  # (1, 2, 3, 4, 5, 6)
print("Original Tuple 1 after concatenation:", tuple1)  # (1, 2, 3)
print("Original Tuple 2 after concatenation:", tuple2)  # (4, 5, 6)

# if we create same variable for concatenation it will be changed due to mutability
"""
l1 = [1,2,3]
l2 = [4,5,6]
l1 = l1 + l2
print("concatenated list: l1 + l2", l1) # [1, 2, 3, 4, 5, 6]
print("original l1:", l1) # [1, 2, 3, 4, 5, 6]
print("original l2:", l2) # [4, 5, 6]
"""