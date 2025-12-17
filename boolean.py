# BOOLEAN (bool) DATA TYPE IN PYTHON

# Boolean has ONLY two values:
# True and False    (Note: Capital T and F)

is_active = True
is_logged_in = False

print(is_active)
print(is_logged_in)

# Check data type
print(type(is_active))      # <class 'bool'>
print(type(is_logged_in))   # <class 'bool'>

# ----------- BOOLEAN FROM COMPARISONS ----------#
# Comparison operators always return boolean

a = 10
b = 20

print(a == b)       # False
print(a != b)       # True
print(a > b)        # False
print(a < b)        # True
print(a >= b)       # True
print(a <= b)       # True

# ----------BOOLEAN FROM LOGICAL OPERATORS ------------ #

# AND Operator
# True only if BOTH conditions are True
print( True and True)   # True
print( True and False)  # False
print( False and True)  # False
print( False and False) # False

# OR Operator
# True if ANY ONE condition is True
print( True or True)   # True
print( True or False)  # True
print( False or True)  # True 
print( False or False) # False

# NOT  Operator
# Reverses the value
print(not True)     # False 
print(not False)    # True 


# ----------- 

age = 18

if age <= 18:
    print("You are eligible to vote")
else: 
    print("You are not eligible to vote")


# ------- VALUES THAT MEAN TRUE AND FALSE IN PYTHON ------- #
# (truthy and Falsy values)

# TRUTHY VALUES (treated as True)
print(bool(True))       # True
print(bool(1))          # True
print(bool(-1))         # True
print(bool(10))         # True
print(bool("Hello"))    # True
print(bool(" "))        # True (space is still a character)
print(bool([1, 2]))     # True
print(bool((0,)))       # True
print(bool({1,3,4}))    # True
print(bool({"a": 1}))   # True

# FALSY VALUES (treated as False)
print(bool(False))      # False
print(bool(0))          # False
print(bool(0.0))        # False
print(bool(""))         # False (empty string)
print(bool([]))         # False (empty list)
print(bool(()))         # False (empty tuple)
print(bool({}))         # False (empty dict)
print(bool(set()))      # False (empty set)
print(bool(None))       # False


# --------- BOOLEAN FROM bool() FUNCTION ------------ #
# bool() converts values into True or False
b1 = bool(100)
print(b1)       # True

b2 = bool("")
print(b2)       # False

b3 = bool("Python")
print(b3)       # True

b4 = bool([])
print(b4)       # False

b5 = bool([0])
print(b5)       # True


#--------------- BOOLEAN RETURNING STRING METHODS ------------- #
# These methods return True or False

text = "Python"

print(text.isupper())       # True
print(text.islower())       # False
print(text.isdigit())       # False
print(text.isalpha())       # False


# ----------- REAL-LIFE BOOLEAN EXAMPLES ---------- #
is_raining = True
has_umbrella = False

if is_raining and has_umbrella:
    print("You can go outside")
else:
    print("Better stay inside")

logged_in = True


if logged_in:
    print("Show dashboard")
else:
    print("Show login page") 


name = rcha
if name == "archa":
    print("Welcome admin")
else:
    print("Welcome User")

    