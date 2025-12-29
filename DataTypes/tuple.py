

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




# -------------------- TUPLE REPETITION ------------------- #

""" 
Notes:
- Can repeat tuples using * operator.
- Create new tuple with repeated elements.
- Useful for initialiation.
"""

repeat_tuple = (1, 2, 3)
print("Original Tuple:", repeat_tuple)          # (1, 2, 3)
print("Repeated Tuple:", repeat_tuple * 3)     # (1, 2, 3, 1, 2, 3, 1, 2, 3)
print("Original Tuple after repetition:", repeat_tuple)  # (1, 2, 3)


# Empty tuple repetition

empty_tuple = ()
print("Empty Tuple repeated 5 times:", empty_tuple * 5)  # ()



# -------------------- Checking element in tuple ------------------- #

"""
Notes:
- Use 'in' keyword to check if element exists in tuple.
- Use 'not in' to check if element does not exist.
- Return True or False.
- Searches through entire tuple (slower for large tuples).
"""

check_tuple = ("apple", "banana", "cherry")
print("banana" in check_tuple)    # True
print("grape" not in check_tuple)  # True
print("grape" in check_tuple)     # False
print("apple" not in check_tuple)   # False



# what is a membership operator



# -------------------- TUPLE METHODS (Only 2 methods) ------------------- #
"""
Notes:
- Tuples have only 2 methods (because they are immutable).
- count(value): returns number of occurrences of a value.
- index(value): returns the index of the first occurrence of a value.\
- No methods for modification (append, remove, etc.) since tuples are immutable.
"""

# count() method
count_tuple = (1, 2, 2, 3, 4, 2, 5)
print("Count of 2 in tuple:", count_tuple.count(2))   # 3
print("Count of 6 in tuple (not in tuple) :", count_tuple.count(6))   # 0

# index() method
index_tuple = ("a", "b", "c", "d", "b")
print("Index of 'b' in tuple:", index_tuple.index("b"))  # 1
# print("Index of 'x' in tuple:", index_tuple.index("x"))  # ValueError: 'x' is not in tuple




# -------------------- TUPLE UNPACKING ------------------- #
"""
Notes:
- tuple unpacking assigns elements to variables.
- Number of variables must match number of tuple elements (or use *).
- Very useful for returning multiple values from functions.
- Makes code more readable and pythonic.
"""

# Basic unpacking
coordinates = (10, 20)
x, y = coordinates
print("Tuple:", coordinates)   # (10, 20)
print("x:", x)                 # 10
print("y:", y)                 # 20


# Unpacking with multiple values
person = ("John", 25, "USA")
name, age, country = person
print("Person Tuple:", person)   # ('John', 25, 'USA')
print("Name:", name)             # John
print("Age:", age)               # 25
print("Country:", country)       # USA

# --------------------- Nested tuple --------------------- #

"""
NOTES:
- Tuples can contain other tuples
- Useful for representing complex data structures
- Access using multiple indices
"""

# 2D tuple (like a matrix)
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print("\nMatrix tuple:")
print(matrix)
print("First row:", matrix[0])
print("Element at [1][2]:", matrix[1][2])
print("Last element:", matrix[2][2])

# Tuple of tuples
student = (
    ("Alice", 20, "A"),
    ("Bob", 22, "B"),
    ("Charlie", 19, "A+")
)

print("Student Tuple:", student)
print("First Student Name:", student[0][0])   # Alice
print("Second Student Age:", student[1][1])    # 22
print("Third Student Grade:", student[1][2])   # B


# Deeply nested tuple
nested_tuple = (1, (2, (3, (4, 5))))
print("Nested Tuple:", nested_tuple)    # (1, (2, (3, (4, 5))))
print("Accessing 4:", nested_tuple[1][1][1][0])  # 4
print("Accessing 5:", nested_tuple[1][1][1][1])  # 5



# --------------------- Tuple Comparison --------------------- #

"""
Notes:
- Tuples can be compared using comparison operators.
- First different elements determine the result.
- If all elements are equal and same length, tuples are equal.
"""


tuple_a = (1, 2, 3)
tuple_b = (1, 2, 4)
tuple_c = (1, 2, 4)
tuple_d = (1, 2)

print("Tuple A:", tuple_a)   # (4, 2, 3)
print("Tuple B:", tuple_b)   # (1, 2, 4)
print("Tuple C:", tuple_c)   # (1, 2, 4)
print("Tuple D:", tuple_d)   # (1, 2)


# Comparison results

# In greater than and less than, it compares element by element from the start.
# If elements are equal, it moves to the next element.
# If all elements are equal but lengths differ, the shorter tuple is considered smaller.

print("tuple_a == tuple_b:", tuple_a == tuple_b)   # False
print("tuple_b == tuple_c:", tuple_b == tuple_c)   # True
print("tuple_b != tuple_d:", tuple_b != tuple_d)   # True
print("tuple_b > tuple_d:", tuple_b > tuple_d)     # True
print("tuple_d < tuple_c:", tuple_d < tuple_c)     # True
print("tuple_a >= tuple_b:", tuple_a >= tuple_b)   # True
print("tuple_d <= tuple_c:", tuple_d <= tuple_c)   # True
print("tuple_a > tuple_c:", tuple_a > tuple_c)     # True

print("tuple_a > tuple_b:", tuple_a > tuple_b)     # False



# String tuple comparison
words1 = ("apple", "banana")
words2 = ("apple", "cherry")
print("\nwords1:", words1)
print("words2:", words2)
print("words1 < words2:", words1 < words2)


# --------------------- Type Conversion to Tuple --------------------- #

"""
NOTES:
- Can convert list to tuple
- Can convert tuple to list
- Can convert string to tuple
- Can convert set to tuple
- Can convert range to tuple
"""


# List to Tuple
list_data = [1, 2, 3, 4, 5]
tuple_from_list = tuple(list_data)
print("List:", list_data)                   # [1, 2, 3, 4, 5]
print("Converted Tuple from List:", tuple_from_list)  # (1, 2, 3, 4, 5)

# Tuple to list
tuple_data = (10, 20, 30)
list_from_tuple = list(tuple_data)
print("Tuple:", tuple_data)                 # (10, 20, 30)
print("Converted List from Tuple:", list_from_tuple)    # [10, 20, 30]

# String to Tuple
string_data = "hello"
tuple_from_string = tuple(string_data)
print("String:", string_data)                # hello
print("Converted Tuple from String:", tuple_from_string)  # ('h', 'e', 'l', 'l', 'o')

# Set to Tuple
set_data = {1, 2, 3}
tuple_from_set = tuple(set_data)
print("Set:", set_data)                      # {1, 2, 3}
print("Converted Tuple from Set:", tuple_from_set)      # (1, 2, 3) (order may vary)

# Range to Tuple
range_data = range(1, 5)
tuple_from_range = tuple(range_data)
print("Range:", list(range_data))            # [1, 2, 3, 4]
print("Converted Tuple from Range:", tuple_from_range)    # (1, 2, 3, 4)

# Dictionary to Tuple (keys)
dict_data = {"a": 1, "b": 2, "c": 3}
tuple_from_dict = tuple(dict_data)
print("Dictionary:", dict_data)              # {'a': 1, 'b': 2, 'c': 3}
print("Converted Tuple from Dictionary (keys):", tuple_from_dict)  # ('a', 'b', 'c') (order may vary)

# Dictionary to Tuple (items)
tuple_from_dict_items = tuple(dict_data.items())
print("Converted Tuple from Dictionary (items):", tuple_from_dict_items)  # (('a', 1), ('b', 2), ('c', 3)) (order may vary)





# ----------------- TUPLE AS DICTIONARY KEY (IMPORTANT USE CASE!) ----------------- #
"""
NOTES:
- Tuples can be used as dictionary keys (lists cannot)
- Must contain only immutable elements
- Useful for composite keys
- Common in real-world applications
"""

# Using tuple as dictionary key
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London",
    (35.6762, 139.6503): "Tokyo"
}
print("\nDictionary with tuple keys:")
print(locations)
print("Location at (51.5074, -0.1278):", locations[(51.5074, -0.1278)])

# Multi-dimensional dictionary
grades = {
    ("Alice", "Math"): 95,
    ("Alice", "Science"): 88,
    ("Bob", "Math"): 82,
    ("Bob", "Science"): 90
}
print("\nStudent grades:")
print("Alice's Math grade:", grades[("Alice", "Math")])
print("Bob's Science grade:", grades[("Bob", "Science")])

# Cannot use list as key
# invalid_dict = {[1, 2]: "value"}  # TypeError: unhashable type: 'list'
print("\nLists cannot be dictionary keys (mutable)")
print("Tuples can be dictionary keys (immutable)")




# ----------------- TUPLE COMPREHENSION (DOESN'T EXIST - RETURNS GENERATOR!) -> Advance concept ----------------- #

"""
NOTES:
- (x for x in ...) creates generator, not tuple
- Use tuple() constructor to convert generator to tuple
- Generator is memory efficient for large datasets
"""

# This creates a generator, not tuple
gen = (x**2 for x in range(5))
print("\nGenerator expression:", gen)
print("Type:", type(gen))

# Convert generator to tuple
squares_tuple = tuple(x**2 for x in range(5))
print("Tuple from generator:", squares_tuple)
print("Type:", type(squares_tuple))

# Comparing memory
import sys
large_tuple = tuple(range(10000))
large_gen = (x for x in range(10000))
print("\nTuple size in bytes:", sys.getsizeof(large_tuple))
print("Generator size in bytes:", sys.getsizeof(large_gen))
print("Generator is much more memory efficient!")


#---------------------- BUILT-IN FUNCTIONS WITH TUPLE --------------------- #

"""
Notes:
- len(): returns number of elements in tuple.
- min(): returns smallest element in tuple.
- max(): returns largest element in tuple.
- sum(): returns sum of numeric elements in tuple.
- sorted(): returns a new sorted list from the tuple elements.
- all(): returns True if all elements are truthy.
- any(): returns True if any element is truthy.
"""

numbers_tuple = (45, 12, 78, 23, 56)
print("\nNumbers tuple:", numbers_tuple)
print("Length:", len(numbers_tuple))
print("Maximum:", max(numbers_tuple))
print("Minimum:", min(numbers_tuple))
print("Sum:", sum(numbers_tuple))
print("Sorted (returns list):", sorted(numbers_tuple))
print("Sorted descending:", sorted(numbers_tuple, reverse=True))

# any() and all()
bool_tuple1 = (True, True, True)
bool_tuple2 = (True, False, True)
bool_tuple3 = (False, False, False)

print("\nbool_tuple1:", bool_tuple1)
print("all():", all(bool_tuple1))
print("any():", any(bool_tuple1))

print("\nbool_tuple2:", bool_tuple2)
print("all():", all(bool_tuple2))
print("any():", any(bool_tuple2))

print("\nbool_tuple3:", bool_tuple3)
print("all():", all(bool_tuple3))
print("any():", any(bool_tuple3))

# Using any() and all() with conditions
numbers = (2, 4, 6, 8, 10)
print("\nNumbers:", numbers)
print("All even?", all(x % 2 == 0 for x in numbers))
print("Any greater than 5?", any(x > 5 for x in numbers))

#==================================================================================
# ADVANTAGES OF TUPLES OVER LISTS -> for extra knowledge
#==================================================================================
"""
NOTES:
ADVANTAGES:
1. Faster than lists (iteration, access)
2. Use less memory than lists
3. Immutable - data protection
4. Can be used as dictionary keys
5. Can be used in sets
6. Safer for data that shouldn't change
7. Better for heterogeneous data

WHEN TO USE TUPLES:
- Data should not change
- Need to use as dictionary key
- Want to ensure data integrity
- Storing related but different types of data
- Returning multiple values from function
- Performance is critical
"""

print("\n--- TUPLE VS LIST COMPARISON ---")

# Memory comparison
import sys
list_data = [1, 2, 3, 4, 5]
tuple_data = (1, 2, 3, 4, 5)

print("List size:", sys.getsizeof(list_data), "bytes")
print("Tuple size:", sys.getsizeof(tuple_data), "bytes")
print("Tuple uses less memory!")

# Tuples in sets (lists cannot be in sets)
set_of_tuples = {(1, 2), (3, 4), (5, 6)}
print("\nSet of tuples:", set_of_tuples)
# set_of_lists = {[1, 2], [3, 4]}  # TypeError: unhashable type: 'list'
print("Lists cannot be added to sets (mutable)")


#==================================================================================
# REAL-LIFE TUPLE EXAMPLES
#==================================================================================
"""
NOTES:
- Tuples are perfect for immutable, related data
- Common in real-world scenarios
"""

# Example 1: RGB Color Values
print("\n--- EXAMPLE 1: RGB COLORS ---")
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

print("Red color:", red)
print("Green color:", green)
print("Accessing red channel:", red[0])

def display_color(color_tuple):
    r, g, b = color_tuple
    print(f"RGB({r}, {g}, {b})")

display_color(blue)

# Example 2: Geographic Coordinates
print("\n--- EXAMPLE 2: COORDINATES ---")
new_york = (40.7128, -74.0060)
london = (51.5074, -0.1278)
tokyo = (35.6762, 139.6503)

cities = {
    new_york: "New York",
    london: "London",
    tokyo: "Tokyo"
}

print("Cities and coordinates:")
for coords, name in cities.items():
    lat, lon = coords
    print(f"{name}: Latitude {lat}, Longitude {lon}")

# Example 3: Date and Time
print("\n--- EXAMPLE 3: DATE REPRESENTATION ---")
date1 = (2025, 12, 23)  # year, month, day
date2 = (2025, 1, 1)

print("Date 1:", date1)
year, month, day = date1
print(f"Formatted: {day}/{month}/{year}")

def format_date(date_tuple):
    y, m, d = date_tuple
    return f"{d:02d}/{m:02d}/{y}"

print("Formatted date:", format_date(date2))

# Example 4: Database Records
print("\n--- EXAMPLE 4: DATABASE RECORDS ---")
employees = [
    (1, "Alice", "Engineering", 75000),
    (2, "Bob", "Marketing", 65000),
    (3, "Charlie", "Sales", 70000),
    (4, "David", "Engineering", 80000)
]

print("Employee Database:")
for emp in employees:
    emp_id, name, dept, salary = emp
    print(f"ID: {emp_id}, Name: {name}, Dept: {dept}, Salary: ${salary}")

# Filter engineers
engineers = [emp for emp in employees if emp[2] == "Engineering"]
print("\nEngineers only:")
for emp in engineers:
    print(emp)

# Example 5: Configuration Settings
print("\n--- EXAMPLE 5: IMMUTABLE CONFIGURATION ---")
# Configuration that should not change
DATABASE_CONFIG = (
    "localhost",    # host
    5432,           # port
    "mydb",         # database name
    "admin"         # username
)

host, port, db_name, user = DATABASE_CONFIG
print(f"Database Config:")
print(f"Host: {host}, Port: {port}, DB: {db_name}, User: {user}")

# Cannot accidentally modify config
# DATABASE_CONFIG[0] = "newhost"  # TypeError
print("Configuration is protected from accidental changes")

#==================================================================================
# END