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


# 1. ------------- LIST INDEXING -------------- #

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

# ----------------- LENGTH OF LIST ----------------- #

"""
Notes:
- Length of list gives the number of elements in the list.
- Use len() function to get length of list."""

my_list = [10, 20, 30, 40, 50]
print("Length of list = ",len(my_list))    # 5

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
# Steps define the no. of elements to skip while slicing.
# Default step is 1.
print(sample_list[0:5:2])   # ['a', 'c', 'e']
print(sample_list[::2])     # ['a', 'c', 'e']
print(sample_list[1::2])    # ['b', 'd']
print(sample_list[0:5:3])   # ['a', 'd']


# Negative Step  --> vvimp
# Reverses the list while slicing
# Default step is -1
print(sample_list[::-1])    # ['e', 'd', 'c', 'b', 'a']  # reverses the list
print(sample_list[::-2])   # ['e', 'c', 'a']
print(sample_list[4:1:-1])  # ['e', 'd', 'c']

# ------------- LIST IS MUTABLE -------------- #

"""
Notes:
- Mutable means we can change the elements of the list.
- We can add, remove, or modify elements in a list.
- Unlike strings, lists can be changed after creation.
"""

nums = [1, 2, 3, 4, 5]
nums[2] = 10   # Changing element at index 2
print(nums)    # [1, 2, 10, 4, 5]

# 2. ------------------ ADDING ELEMENTS TO LIST ------------------ #

# ADDING ELEMENTS TO LIST USING append() AND insert() METHODS

"""
 1. append(value)
 2. insert(index, value)
"""

"""
Notes:
- append() , insert() methods are used to add elements to a list.
- append() adds an element at the end of the list.
- insert(index, value) adds an element at a specific index.
"""

# 2.1 append() method

colors = ["red", "green", "blue"]
colors.append("yellow")
print(colors)   # ['red', 'green', 'blue', 'yellow']


# 2.2 insert() method

colors.insert(1, "orange")
print(colors)   # ['red', 'orange', 'green', 'blue', 'yellow']


# if we try to insert a value at an index which we don't have , it adds at the end
colors.insert(10, "purple")
print(colors)   # ['red', 'orange', 'green', 'blue', 'yellow', 'purple']


# 3. ---------------- REMOVING ELEMENTS FROM LIST ------------------ #

# REMOVING ELEMENTS USING remove() AND pop() METHODS

"""
 1. remove(value)
 2. pop()
 3. pop(index)
 4. clear()
"""

"""
Notes:
- remove(value) : removes the first occurrence of the specified value from the list.
- pop() : removes and returns the last element of the list.
- pop(index) : removes and returns the element at the specified index.
- clear() : removes all elements from the list.
- del keyword to delete entire list or a portion of the list using slicing
- if we try to remove an item not in the list using remove(), it gives ValueError

"""

# 3.1 remove() method

# if there are duplicate values, only first occurrence is removed
names = ["Alice", "Bob", "Charlie", "Bob"]
names.remove("Bob")
print(names)   # ['Alice', 'Charlie', 'Bob']

# names.remove("David")  # ValueError: list.remove(x): x not in list

# 3.2 pop() method

# pop() without index
# - removes last element
fruits = ["apple", "banana", "cherry"]
last_fruit = fruits.pop()
print("Removed = ",last_fruit)   # cherry
print(fruits)   # ['apple', 'banana']

# pop() with index
# - removes element at specified index
first_fruit = fruits.pop(0)
print("Removed = ",first_fruit)   # apple
print(fruits)   # ['banana']

# 3.3 clear() method
# clears the entire list
fruits.clear()
print(fruits)   # []

# 3.4 Using del keyword

# del keyword to delete entire list
# permanently deletes the list
# syntax: del list_name[index]  to delete element at index
# del slicing to delete a portion of the list

colors = ["red", "green", "blue", "yellow", "purple"]
del colors[1:4]
print(colors)  #['red', 'purple']

del colors
# print(colors)  # gives NameError as colors is deleted


# 4. ------------------ SORTING A LIST ------------------ #

# SORTING A LIST USING sort() METHOD

"""
Notes:
- sort() method sorts the list in ascending order by default.
- sort(reverse=True) sorts the list in descending order.
- Works only when elements are comparable.
"""

numbers = [50, 20, 40, 10, 30]

# Sorting in ascending order
numbers.sort()
print("Ascending order:", numbers)   # [10, 20, 30, 40, 50]

# Sorting in descending order
numbers.sort(reverse=True)
print("Descending order:", numbers)  # [50, 40, 30, 20, 10]


# 5 -------------- REVERSING A LIST --------------- #

# REVERSING A LIST USING reverse() METHOD

"""
Notes:
- reverse() method reverses the order of elements in the list.
- It does not sort the list, just reverses the current order.
"""

chars = ['a', 'b', 'c', 'd', 'e']
chars.reverse()
print("Reversed list:", chars)   # ['e', 'd', 'c', 'b', 'a']




# 6. --------------- COPYING A LIST --------------- #

# COPYING A LIST USING ASSIGNMENT AND copy() METHOD

"""
Notes:
- copy() method creates a shallow copy of the list.
- Assignment creates a reference to the same list.
"""

a = [1, 2, 3]
b = a
b.append(4)
print("a:", a)  # [1, 2, 3, 4] both a and b refer to same list
print("b:", b)  # [1, 2, 3, 4]   

c = a.copy()
c.append(5)
print("a:", a)  # [1, 2, 3, 4]
print("c:", c)  # [1, 2, 3, 4, 5] c is a separate copy

# change in copy does not affect original list


#homework 
#what is shallow copy vs deep copy
#what is reference vs copy
#list comprehenshion
#how range works
#anyother built in functions


#list concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)  #[1, 2, 3, 4, 5, 6]

#list repetition
repeated = list1 * 3
print(repeated)  #[1, 2, 3, 1, 2, 3, 1, 2, 3]



#bucket 7
#count and index methods

numbers = [1, 2, 3, 2, 4, 2, 5]

print(numbers.count(2))  #3 (counts occurrences of 2)

print(numbers.index(4))  #4 (index of first occurrence of 4)


#checkiing elemeent inside list, membership operators
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)   #True
print("grape" not in fruits) #True
print("grape" in fruits)    #False
print("apple" not in fruits)  #False



#nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
print(matrix[0])      #[1, 2, 3] first row
print(matrix[1][2])   #6 element at row 1, column 2


#list comprehension

squares = [i * i for i in range(1, 6)]
print(squares)  #[1, 4, 9, 16, 25]

even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)  #[2, 4, 6, 8, 10]


#type conversion to list


#bucket 

#built-in functions with lists
2
numbers = [10, 20, 5, 15]
print(sum(numbers))   #50
print(min(numbers))   #5
print(max(numbers))   #20
print(len(numbers))   #4


#bucket

#any() and all()
num = [0, 1, 2, 3]
print(any(num))  #True (at least one non-zero)
print(all(num))  #False (not all non-zero)
print(all(i % 2 == 0 for i in num))  #False (not all even)
print(any(i > 2 for i in num))  #True (at least one greater than 2)


#real world examples of lists
mark = [85, 90, 78, 92, 88]  #marks of a student in different subjects
total_marks = sum(mark)
average = total_marks / len(mark)
print("Total Marks:", total_marks)    #Total Marks: 433
print("Average Marks:", average)      #Average Marks: 86.6

cart = ["apple", "banana", "orange"]
cart.append("grape")
print("Shopping Cart:", cart)  #Shopping Cart: ['apple', 'banana', 'orange', 'grape']