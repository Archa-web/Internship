# HOMEWORK 

age = 18
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

age = 16
name1 = "Alice"
if age >= 18 and name1 == "Alice":
    print("Welcome Alice, you are eligible to vote")
else:
    print("You are not eligible to vote or name mismatch")

fruit = "banana"
if fruit == "apple" or fruit == "banana":
    print("You selected a fruit we have")
else:
    print("Fruit not available")

score = 85
if not score < 50:
    print("You passed the exam")
else:
    print("You failed the exam")

admin = 101
hr = 102
employee1 = 103
employee2 = 104

if  admin == 101 or hr == 102:
    print("Welcome Admin/HR")
elif employee1 == 103 or employee2 == 104:
    print("Welcome Employee")

# Comparison with string

name = "rcha"
if name == "archa":
    print("Welcome admin")
else:
    print("Welcome User")

name = "rcha"
if name != "archa":
    print("Welcome admin")
else:
    print("Welcome User")
    

# how with works with <, >, <=, >=

name1 = "alice"
name2 = "bob"
if name1 <= name2:
    print(f"{name1} comes before {name2} alphabetically")
else:
    print(f"{name2} comes before {name1} alphabetically")

name11 = "Charlie"
name22 = "bob"
if name11 < name22:
    print(f"{name11} comes after {name22} alphabetically")
else:
    print(f"{name22} comes after {name11} alphabetically")



# homework
# create a tuple with different data types and perform all types of built-in operations on it.


# why tuple is faster than list?
# Because tuples are immutable, Python can optimize their storage and access.


