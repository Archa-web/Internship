#==================================================================================
# SET (set) DATA TYPE IN PYTHON
#==================================================================================
"""
NOTES:
- Set is an unordered collection of unique elements
- Set is mutable (changeable) but elements must be immutable
- Set does NOT allow duplicate values (automatically removes duplicates)
- Set does NOT maintain insertion order (unordered)
- Set is written using curly braces {}
- Set does NOT support indexing or slicing (because it's unordered)
- Set elements must be immutable (can't add list, dict, or set as elements)
"""

# Creating sets
numbers_set = {1, 2, 3, 4, 5}
names_set = {"Alice", "Bob", "Charlie"}
mixed_set = {1, "Python", 3.14, True}  # Can mix types but elements must be immutable

print("Numbers set:", numbers_set)      # {1, 2, 3, 4, 5}
print("Names set:", names_set)          # {'Alice', 'Bob', 'Charlie'}
print("Mixed set:", mixed_set)          # {1, 'Python', 3.14, True}

# Check data type
print("Type of numbers_set:", type(numbers_set))    # <class 'set'>

# Sets automatically remove duplicates
duplicate_set = {1, 2, 2, 3, 3, 3, 4}
print("Set with duplicates removed:", duplicate_set)    # {1, 2, 3, 4}




#==================================================================================
# EMPTY SET
#==================================================================================
"""
NOTES:
- Empty set must be created using set() function
- {} creates an empty dictionary, NOT an empty set
- Used when unique elements will be added later dynamically
"""

empty_set = set()
print("Empty set:", empty_set)              # set() 
print("Type of empty set:", type(empty_set))    # <class 'set'>

# This creates a dictionary, not a set
not_a_set = {}
print("Empty dictionary (not set):", type(not_a_set))   # <class 'dict'>




#==================================================================================
# SET DOES NOT SUPPORT INDEXING OR SLICING
#==================================================================================
"""
NOTES:
- Sets are unordered, so no indexing or slicing
- It will show TypeError if attempted
- Cannot access elements by position
"""

sample_set = {10, 20, 30, 40, 50}
# print(sample_set[0])  # TypeError: 'set' object is not subscriptable
# print(sample_set[1:3])  # TypeError: 'set' object is not subscriptable

print("Cannot use indexing on sets - sets are unordered")




#==================================================================================
# LENGTH OF SET
#==================================================================================
"""
NOTES:
- len() returns number of unique elements in the set
"""

my_set = {10, 20, 30, 40, 50}
print("Length of set:", len(my_set))    # 5

duplicate_check = {1, 1, 2, 2, 3, 3}
print("Length after removing duplicates:", len(duplicate_check))    # 3



#==================================================================================
# SET IS MUTABLE (BUT ELEMENTS MUST BE IMMUTABLE)
#==================================================================================
"""
NOTES:
- Set itself can be modified (add/remove elements)
- But elements inside set must be immutable
- Cannot add list, dict, or set as elements
- Can add int, float, string, tuple, frozenset
"""

mutable_set = {1, 2, 3}
mutable_set.add(4)
print("Set after adding element:", mutable_set)     # {1, 2, 3, 4}

# Valid immutable elements
valid_set = {1, "text", 3.14, (1, 2), True}
print("Set with valid immutable elements:", valid_set)      # {1, 'text', 3.14, (1, 2), True}

# Invalid - cannot add mutable elements
# invalid_set = {1, 2, [3, 4]}  # TypeError: unhashable type: 'list'
# invalid_set = {1, 2, {3, 4}}  # TypeError: unhashable type: 'set'
print("Cannot add mutable elements like lists or sets inside sets")



#==================================================================================
# ADDING ELEMENTS TO SET
#==================================================================================
"""
NOTES:
- add() - adds single element to the set
- update() - adds multiple elements from iterable
- If element already exists, set remains unchanged (no duplicates)
"""

# Using add()
nums_set = {1, 2, 3}
nums_set.add(4)
print("After add(4):", nums_set)    # {1, 2, 3, 4}

nums_set.add(2)  # Adding duplicate - no effect
print("After add(2) - duplicate ignored:", nums_set)    # {1, 2, 3, 4}

# Using update() - adds multiple elements
nums_set.update([5, 6, 7])
print("After update([5, 6, 7]):", nums_set)     # {1, 2, 3, 4, 5, 6, 7}

nums_set.update({8, 9}, [10, 11])
print("After update with multiple iterables:", nums_set)    # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

# Update with string (adds each character)
char_set = {'a', 'b'}
char_set.update("cd")
print("After update('cd'):", char_set)   # {'a', 'b', 'c', 'd'}



#==================================================================================
# REMOVING ELEMENTS FROM SET
#==================================================================================
"""
NOTES:
- remove(value) - removes element, raises KeyError if not found
- discard(value) - removes element, does nothing if not found
- pop() - removes and returns random element (set is unordered)
- clear() - removes all elements
- del - deletes entire set(no indexing or slicing)
"""

# Using remove()
fruits = {"apple", "banana", "cherry", "date"}
fruits.remove("banana")
print("After remove('banana'):", fruits)        # {'apple', 'cherry', 'date'}

# fruits.remove("grape")  # KeyError: 'grape' - element not found
print("remove() raises KeyError if element not found")

# Using discard() - safer, no error if element doesn't exist
fruits.discard("cherry")
print("After discard('cherry'):", fruits)         # {'apple', 'date'}

fruits.discard("grape")  # No error
print("After discard('grape') - no error:", fruits)         # {'apple', 'date'}

# Using pop() - removes random element
numbers = {10, 20, 30, 40, 50}
removed = numbers.pop()
print("Popped element:", removed)           # {20}
print("Set after pop():", numbers)          # {10, 30, 40, 50}

# Using clear()
temp_set = {1, 2, 3, 4, 5}
temp_set.clear()
print("Set after clear():", temp_set)       # set()

# Using del - deletes entire set
del_set = {1, 2, 3}
del del_set
# print(del_set)                             # NameError: name 'del_set' is not defined
print("Set deleted using del")              



#==================================================================================
# CHECKING ELEMENT IN SET (MEMBERSHIP OPERATORS)
#==================================================================================
"""
NOTES:
- 'in' operator checks if element exists
- 'not in' operator checks if element doesn't exist
- Very fast operation - O(1) time complexity
- More efficient than checking in list
"""

colors = {"red", "green", "blue", "yellow"}
print("Is 'red' in colors?", "red" in colors)                   # True
print("Is 'purple' in colors?", "purple" in colors)             # False
print("Is 'purple' not in colors?", "purple" not in colors)     # True




#==================================================================================
# SET OPERATIONS (MATHEMATICAL SET OPERATIONS)
#==================================================================================
"""
NOTES:
- Union: all elements from both sets
- Intersection: common elements in both sets
- Difference: elements in first set but not in second
- Symmetric Difference: elements in either set but not both
"""

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union - combines all elements (no duplicates)
print("\n--- UNION ---")
print("set_a:", set_a)          # {1, 2, 3, 4, 5}
print("set_b:", set_b)          # {4, 5, 6, 7, 8}
print("Union using | operator:", set_a | set_b)         # {1, 2, 3, 4, 5, 6, 7, 8}
print("Union using union():", set_a.union(set_b))       # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection - common elements
print("\n--- INTERSECTION ---")
print("Intersection using & operator:", set_a & set_b)                  # {4, 5}
print("Intersection using intersection():", set_a.intersection(set_b))    # {4, 5}

# Difference - elements in first set but not in second
print("\n--- DIFFERENCE ---")
print("set_a - set_b:", set_a - set_b)                          # {1, 2, 3}
print("set_a.difference(set_b):", set_a.difference(set_b))      # {1, 2, 3}
print("set_b - set_a:", set_b - set_a)                          # {6, 7, 8}

# Symmetric Difference - elements in either set but not both  -> excludes all elemnts in common
print("\n--- SYMMETRIC DIFFERENCE ---")
print("Symmetric difference using ^ operator:", set_a ^ set_b)                                      # {1, 2, 3, 6, 7, 8}
print("Symmetric difference using symmetric_difference():", set_a.symmetric_difference(set_b))      # {1, 2, 3, 6, 7, 8}


#==================================================================================
# COPYING SETS
#==================================================================================
"""
NOTES:
- copy() creates shallow copy
- Assignment (=) creates reference, not copy
"""

original_set = {1, 2, 3}
reference_set = original_set  # Reference, not copy
reference_set.add(4)
print("\nOriginal set after modifying reference:", original_set)    # {1, 2, 3, 4}
print("Reference set:", reference_set)                # {1, 2, 3, 4}    

original_set2 = {1, 2, 3}
copied_set = original_set2.copy()  # Creates actual copy
copied_set.add(5)
print("\nOriginal set2:", original_set2)        # {1, 2, 3}
print("Copied set:", copied_set)                # {1, 2, 3, 5}

#==================================================================================
# FROZEN SET (IMMUTABLE SET)
#==================================================================================
"""
NOTES:
- frozenset is immutable version of set
- Cannot add, remove, or modify elements
- Can be used as dictionary key or set element
"""

frozen = frozenset([1, 2, 3, 4, 5])
print("\nFrozen set:", frozen)              # frozenset({1, 2, 3, 4, 5})
print("Type:", type(frozen))            # <class 'frozenset'>

# frozen.add(6)  # AttributeError: 'frozenset' object has no attribute 'add'
# frozen.remove(1)  # AttributeError: 'frozenset' object has no attribute 'remove'

# Can use frozen set as dictionary key
dict_with_frozenset = {frozen: "This is valid"}
print("Dictionary with frozenset as key:", dict_with_frozenset)         # {frozenset({1, 2, 3, 4, 5}): 'This is valid'}

# Can use frozen set as set element
set_of_frozensets = {frozenset([1, 2]), frozenset([3, 4])}          
print("Set of frozensets:", set_of_frozensets)                          # {frozenset({1, 2}), frozenset({3, 4})}

# Frozen set supports read-only operations
frozen1 = frozenset([1, 2, 3])
frozen2 = frozenset([2, 3, 4])
print("Union of frozensets:", frozen1 | frozen2)                    # frozenset({1, 2, 3, 4})   
print("Intersection of frozensets:", frozen1 & frozen2)             # frozenset({2, 3})
print("Difference of frozensets:", frozen1 - frozen2)               # frozenset({1})
print("Symmetric difference of frozensets:", frozen1 ^ frozen2)     # frozenset({1, 4})

#==================================================================================
# CONVERTING BETWEEN DATA TYPES
#==================================================================================
"""
NOTES:
- Can convert list to set (removes duplicates)
- Can convert tuple to set
- Can convert string to set (gets unique characters)
- Can convert set back to list or tuple
"""

# List to Set
list_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_set = set(list_with_duplicates)
print("\nList with duplicates:", list_with_duplicates)              # [1, 2, 2, 3, 3, 3, 4, 5, 5]
print("Converted to set (duplicates removed):", unique_set)         # {1, 2, 3, 4, 5}

# Tuple to Set
tuple_data = (1, 2, 2, 3, 3, 4)
set_from_tuple = set(tuple_data)
print("Tuple:", tuple_data)                                 # (1, 2, 2, 3, 3, 4)
print("Converted to set:", set_from_tuple)                  # {1, 2, 3, 4}

# String to Set (gets unique characters)
text = "hello world"
char_set = set(text)
print("String:", text)                       # hello world
print("Unique characters in set:", char_set)    # {'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'}

# Set to List
my_set = {5, 3, 1, 4, 2}
list_from_set = list(my_set)
print("Set:", my_set)                       # {1, 2, 3, 4, 5}
print("Converted to list:", list_from_set)      # [1, 2, 3, 4, 5] (order may vary)

#==================================================================================
# SET COMPREHENSION
#==================================================================================
"""
NOTES:
- Similar to list comprehension but creates set
- Automatically removes duplicates
- Uses curly braces {}
"""

# Basic set comprehension
squares_set = {x**2 for x in range(1, 6)}
print("\nSquares set using comprehension:", squares_set)        # {1, 4, 9, 16, 25}

# Set comprehension with condition
even_squares = {x**2 for x in range(1, 11) if x % 2 == 0}
print("Even squares:", even_squares)             # {4, 16, 36, 64, 100}

# Remove duplicates using set comprehension
numbers_list = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique_numbers = {x for x in numbers_list}
print("Unique numbers from list:", unique_numbers)      # {1, 2, 3, 4, 5}

# Set comprehension with string
vowels = {char for char in "hello world" if char in "aeiou"}
print("Vowels from 'hello world':", vowels)        # {'e', 'o'}

#==================================================================================
# BUILT-IN FUNCTIONS WITH SETS
#==================================================================================
"""
NOTES:
- len() - number of elements
- sum() - sum of numeric elements
- max() - maximum element
- min() - minimum element
- sorted() - returns sorted list
- any() - True if any element is True
- all() - True if all elements are True
"""

numbers_set = {10, 20, 30, 40, 50}
print("\nNumbers set:", numbers_set)                            # {10, 20, 30, 40, 50}
print("Length:", len(numbers_set))                              # 5
print("Sum:", sum(numbers_set))                                 # 150
print("Maximum:", max(numbers_set))                             # 50
print("Minimum:", min(numbers_set))                             # 10
print("Sorted (returns list):", sorted(numbers_set))            # [10, 20, 30, 40, 50]
print("Sorted in reverse:", sorted(numbers_set, reverse=True))  # [50, 40, 30, 20, 10]

# any() and all()
set1 = {2, 4, 6, 8, 10}
set2 = {1, 2, 3, 4, 5}
print("\nset1:", set1)                                                  # {2, 4, 6, 8, 10}
print("Are all elements even?", all(x % 2 == 0 for x in set1))          # True
print("\nset2:", set2)                                                  # {1, 2, 3, 4, 5}
print("Is any element greater than 4?", any(x > 4 for x in set2))       # True

#==================================================================================
# WHEN TO USE SETS VS LISTS
#==================================================================================
"""
NOTES:
USE SETS WHEN:
- Need to store unique elements only
- Order doesn't matter
- Need fast membership testing (checking if element exists)
- Need to remove duplicates from data

USE LISTS WHEN:
- Need to maintain order
- Need to allow duplicates
- Need to access elements by index
- Need to store mutable elements
"""

print("\n--- PERFORMANCE COMPARISON ---")
# Membership testing is faster in sets
large_list = list(range(100000))
large_set = set(range(100000))

# Checking membership
print("Checking '99999 in list' vs '99999 in set'")
print("Set membership is much faster (O(1) vs O(n))")

#==================================================================================
# REAL-LIFE SET EXAMPLES
#==================================================================================
"""
NOTES:
- Sets are perfect for real-world scenarios requiring uniqueness
"""

# Example 1: Removing duplicate emails
print("\n--- EXAMPLE 1: REMOVING DUPLICATE EMAILS ---")
email_list = ["john@example.com", "jane@example.com", "john@example.com", 
              "alice@example.com", "jane@example.com"]
unique_emails = set(email_list)
print("Original email list:", email_list)
print("Unique emails:", unique_emails)
print("Number of unique subscribers:", len(unique_emails))

# Example 2: Finding common interests
print("\n--- EXAMPLE 2: FINDING COMMON INTERESTS ---")
alice_interests = {"reading", "hiking", "coding", "gaming"}
bob_interests = {"coding", "gaming", "cooking", "traveling"}
common_interests = alice_interests & bob_interests
print("Alice's interests:", alice_interests)
print("Bob's interests:", bob_interests)
print("Common interests:", common_interests)

# Example 3: Tracking unique visitors
print("\n--- EXAMPLE 3: TRACKING UNIQUE WEBSITE VISITORS ---")
visitors_monday = {"user1", "user2", "user3", "user4"}
visitors_tuesday = {"user3", "user4", "user5", "user6"}
all_unique_visitors = visitors_monday | visitors_tuesday
returning_visitors = visitors_monday & visitors_tuesday
new_visitors_tuesday = visitors_tuesday - visitors_monday

print("Monday visitors:", visitors_monday)
print("Tuesday visitors:", visitors_tuesday)
print("Total unique visitors:", all_unique_visitors)
print("Returning visitors:", returning_visitors)
print("New visitors on Tuesday:", new_visitors_tuesday)

# Example 5: Finding unique words in text
print("\n--- EXAMPLE 5: UNIQUE WORDS IN TEXT ---")
text = "the quick brown fox jumps over the lazy dog the fox was quick"
words = text.split()
unique_words = set(words)
print("Text:", text)
print("Total words:", len(words))
print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))

# Example 6: Product tags
print("\n--- EXAMPLE 6: PRODUCT TAGS ---")
product1_tags = {"electronics", "smartphone", "android", "sale"}
product2_tags = {"electronics", "smartphone", "ios", "premium"}
all_tags = product1_tags | product2_tags
common_tags = product1_tags & product2_tags

print("Product 1 tags:", product1_tags)
print("Product 2 tags:", product2_tags)
print("All available tags:", all_tags)
print("Common tags:", common_tags)

# Example 7: Attendance tracking
print("\n--- EXAMPLE 7: CLASS ATTENDANCE ---")
registered_students = {"Alice", "Bob", "Charlie", "David", "Eve"}
present_students = {"Alice", "Charlie", "David"}
absent_students = registered_students - present_students

print("Registered students:", registered_students)
print("Present students:", present_students)
print("Absent students:", absent_students)
print("Attendance rate:", f"{len(present_students)/len(registered_students)*100:.1f}%")