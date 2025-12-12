"""
1. Numeric Types
    int = integer numbers (10, -5, 0)
    float = floating-point numbers (3.14, -0.5)
    complex = complex numbers (2 + 3j)

2. Boolean Type
    bool = True or False

3. Text Type
    str = string (text)    

4. Sequence Types
    list = ordered, changable list, []
    tuple = ordered, unchangable list, ()

5. Set Types
    set = unordered unique values, {}

6. Mapping Type
    dict = key-value pairs (k:v)

"""

#  INT (INTEGER) DATA TYPE IN PYTHON

# int means: whole numbers without decimal point
a = 10
b = -20
c = 0

print(a, b, c)

# To check the data type
print(type(a))  # <class 'int'>
print(type(b))  # <class 'int'>
print(type(c))  # <class 'int'>

#-------- BASIC ARITHMETIC OPERATIONS WITH int--------#

a = 10
b = 3

# Addition
print(a + b)  #13

# Subtraction
print(a - b)  # 7

# Multiplication
print(a * b)  # 30

# Division - / vs //
print(a / b)    # 3.33333333 (normal division, result is float)
print(a // b)   # 3          (floor division, result is int)

# / -> normal division ( can give decimal)
# // -> "cut off" the decimal part (floor division)

#Remainder (Modulo)
print(a % b)  # 1

# % gives remainder after division.

#Power (Exponent)
print(a ** b) # 10 ** 3 = 1000

#Comparison Operations
x = 10
y = 20
print(x == y)  #Equal to
print(x != y)  #Not equal to
print(x > y)   #Greater than
print(x < y)   #Less than
print(x >= y)  #Greater than or equal to
print(x <= y)  #Less than or equal to

#Type Conversion(Casting)
#float to int
f1 = 10.5
f2 = -3.7

print(int(f1)) #10
print(int(f2)) #-3

#string to int
s1 = "25"
s2 = "-7"
print(int(s1)) #25
print(int(s2)) #-7

#invalid string to int
s3 = "Hello"
# print(int(s3)) #ValueError: invalid literal for int() with base 10
a="10.5"
# print(int(a)) #ValueError: invalid literal for int() with base 10

#FLOAT
#Numbers with decimal point
x = 10.5
y = -3.14
z = 0.0
print(x)
print(y)
print(z)
print(type(x)) #class 'float'
print(type(y)) #class 'float'
print(type(z)) #class 'float'

#ARITHMETIC OPERATIONS ON FLOATS
a = 5.5
b = 2.0
print(a + b)  #Addition
print(a - b)  #Subtraction
print(a * b)  #Multiplication
print(a / b)  #Division
print(a // b) #Floor Division
print(a % b)  #Modulus
print(a ** b) #Exponentiation
#Always get float as result

#Mixed Operations
x = 10    #int
y = 3.5   #float
print(x + y)  #Addition
print(x - y)  #Subtraction
print(x * y)  #Multiplication
print(x / y)  #Division
#Output will be float

#Comparison Operations
p = 7.5
q = 10.0
print(p == q)  #Equal to
print(p != q)  #Not equal to
print(p > q)   #Greater than
print(p < q)   #Less than
print(p >= q)  #Greater than or equal to
print(p <= q)  #Less than or equal to

#Type Conversion(Casting)
#int to float
i1 = 10
i2 = -5
print(float(i1)) #10.0
print(float(i2)) #-5.0
#string to float
s1 = "12.34"
s2 = "-7.89"
print(float(s1)) #12.34
print(float(s2)) #-7.89
#invalid string to float
s3 = "World"
# print(float(s3)) #ValueError: could not convert string to float: 'World
s4 = "156abc"
# print(float(s4)) #ValueError: could not convert string to float: '15.6abc'

#built-in functions for floats
pi = 3.14159
print(round(pi))      #Rounds to nearest integer
print(round(pi, 2))   #Rounds to 2 decimal places

#precision issues
a = 0.1 + 0.2
print(a)              #0.30000000000000004
print(round(a, 2))  #0.3    

"""COMPLEX NUMBERS (complex) IN PYTHON

Complex number: a + bj
a → real part (int or float)
b → imaginary part (int or float)
j → imaginary unit (√-1)

Creating complex numbers

z1 = 2 + 3j real = 2, imaginary = 3
z2 = -1 - 4j
z3 = 5.0 + 0j real part float
z4 = 0 + 2j only imaginary

print(z1, z2, z3, z4)

Check data type
print(type(z1)) <class 'complex'>

Accessing real and imaginary parts
print(z1.real) 2.0
print(z1.imag) 3.0

print(z2.real) -1.0
print(z2.imag) -4.0

BASIC OPERATIONS WITH COMPLEX NUMBERS

a = 2 + 3j
b = 1 - 4j

Addition
print(a + b) (3-1j)

Subtraction
print(a - b) (1+7j)

Multiplication
print(a * b) (14-5j)

Division
print(a / b) (-0.5882352941176471 + 0.6470588235294118j) approx

Conjugate of a complex number
For z = a + bj, conjugate is a - bj
z = 3 + 4j
print(z.conjugate()) (3-4j)

Mixing with int and float

x = 5 int
y = 2.5 float
z = 3 + 4j complex

print(x + z) (8+4j)
print(y + z) (5.5+4j)

Note: if you mix int/float with complex, result becomes complex

Using complex numbers in simple examples

Example 1: Electrical engineering (impedance)

r = 4 resistance (real part)
x_react = 3 reactance (imaginary part)
impedance = complex(r, x_react) 4 + 3j
print("Impedance:", impedance)

Example 2: Distance from origin in complex plane

point = 3 + 4j
distance = abs(point) same as sqrt(3^2 + 4^2)
print("Distance from origin:", distance) 5.0
"""

#String Data Type (str)
#Strings are sequences of characters enclosed in single quotes(' '), double quotes(" "), or triple
empty_string = ""

#multi line string using triple quotes
multi_line_string = """This is a multi-line
string that spans multiple lines."""    
print(empty_string)
print(multi_line_string)
print(type(empty_string)) #class 'str'
print(type(multi_line_string)) #class 'str'

#single quote string and double quote string
single_quote_str = 'Hello, World!'
double_quote_str = "Python is awesome!"
print(single_quote_str)
print(double_quote_str)

#length of string
str1 = "Hello"
print(len(str1)) #5
str2 = "Python Programming"
print(len(str2)) #18

#indexing
#it is to get position of character in string
sample_str = "Python"
print(sample_str[0])  #P
print(sample_str[3])  #h
print(sample_str[2])  #n
print(sample_str[4])  #IndexError: string index out of range
#indexing starts from 0

first_char = sample_str[0]
second_char = sample_str[1]
third_char = sample_str[2]  
fourth_char = sample_str[3]
last_char = sample_str[4]
print(first_char)  #P
print(second_char) #y
print(third_char)  #t
print(fourth_char) #h
print(last_char)   #n
#last index is length-1
#P -- 0
#y -- 1
#t -- 2
#h -- 3
#o -- 4
#n -- 5

#negative indexing
print(sample_str[-1]) #n
print(sample_str[-3]) #h
print(sample_str[-6]) #P
# print(sample_str[-7]) # IndexError

#-1 refers to last character
first_char_neg = sample_str[-6]
second_char_neg = sample_str[-5]
third_char_neg = sample_str[-4]
fourth_char_neg = sample_str[-3]
last_char_neg = sample_str[-1]
print(first_char_neg)  #P
print(second_char_neg) #y
print(third_char_neg)  #t
print(fourth_char_neg) #h
print(last_char_neg)   #n

#P -- 0 -- -6
#y -- 1 -- -5
#t -- 2 -- -4
#h -- 3 -- -3
#o -- 4 -- -2
#n -- 5 -- -1

# 1. Changing case of string
text = "Hello, World!"
print(text.upper()) #HELLO, WORLD! upper case
print(text.lower()) #hello, world! lower case
print(text.capitalize()) #Hello, world! first letter capitalized
print(text.title()) #Hello, World! first letter of each word capitalized

# 2. Removing whitespace
text_with_spaces = "   Hello, Python!   "
stripped_text = text_with_spaces.strip()
print(stripped_text) #"Hello, Python!" without leading/trailing spaces

#removing leading whitespace
leading_stripped = text_with_spaces.lstrip()
print(leading_stripped) #"Hello, Python!   " without leading spaces     

#removing trailing whitespace
trailing_stripped = text_with_spaces.rstrip()
print(trailing_stripped) #"   Hello, Python!" without trailing spaces   

# 3. Inding substrings
main_str = "Hello, Hello welcome to Python programming."
#finding first occurrence of substring
#case-sensitive
#return -1 if not found

index = main_str.find("Python")
print(index) #18 
index_not_found = main_str.find("Java")
print(index_not_found) #-1

# 4. Replacing substrings
#it need 2 parameters: old substring and new substring
#replacing all occurrences of a substring with another substring
original_str = "I like apples. Apples are my favorite fruit."
#case-sensitive
new_str = original_str.replace("apples", "oranges")
print(new_str) #"I like oranges. Apples are my favorite fruit."


#5 bucket
#bucket 5.1
# 5. Checking what string contains (return True / False)
str_alpha = "HelloWorld"
print(str_alpha.isalpha()) #True
str_alpha_num = "Hello123"
print(str_alpha_num.isalpha()) #False
print("Hello World".isalpha()) #False (space is not alphabetic)

#check if all characters are numeric
str_numeric = "12345"
print(str_numeric.isdigit()) #True
str_mixed = "123abc"
print(str_mixed.isdigit()) #False
print("5 bucket".isdigit()) #False

#check if all characters are alphanumeric (letters and numbers only no special characters)
#returns True if all characters are alphanumeric and there is at least one character
#otherwise False
#returns False for empty string
str_alnum = "Hello123"
print(str_alnum.isalnum()) #True
str_special = "Hello@123"
print(str_special.isalnum()) #False
print("5bucket".isalnum()) #True

#bucket 5.2
#isupper() method and islower() method
upper_str = "HELLO"
lower_str = "hello"
mixed_str = "Hello"
print(upper_str.isupper()) #True
print(lower_str.islower()) #True
print(mixed_str.isupper()) #False
print(mixed_str.islower()) #False
print("5BUCKET".isupper()) #True
print("5bucket".islower()) #True
#special example
special_str = "HELLO123!"
print(special_str.isupper()) #True (numbers and special characters are ignored)
special_str2 = "hello@world"
print(special_str2.islower()) #True (numbers and special characters are ignored)


#isspace() method
# Checks if string contains only whitespace  
space_str = "   "
non_space_str = " Hello "
empty_str = ""
print(space_str.isspace()) #True
print(non_space_str.isspace()) #False
print(empty_str.isspace()) #False
print("     \t\n".isspace()) #True (contains only whitespace characters)

# 6. Splitting and joining strings

# 6.1 (split)
# When we split a string, is becomes a list of substrings
# When there is no parameter given to split(), it splits by whitspace by default
sample_str = "Hello world! Welcome to python program"
# Splitting the string into a list of words
word_list = sample_str.split()   # Split by space
print("List of words:",word_list)

fruits_str = "apple,banana,cherry,date"
# Splitting the string into a list of fruits using comma as separator
fruits_list = fruits_str.split(",") # Split by comma
print("List of fruits:", fruits_list)

# 6.2 (join)
# Joining the list of words back into a string a single string
# When we join it become a single string again
# We can specify the joiner while joining
#It doesn't have any default separator in the beginning
joined_str = " ".join(word_list)    #Join with space
print("Joined string:", joined_str)

joined_str_comma = ",".join(fruits_list)    #Join with comma
print("Joined string:", joined_str_comma)   


# 7. stratswith() and endswith() method
# It checks if the string starts or ends with the specified substring
# Itreturn True or False
# This is case-sensitive
test_str = "Hello, welcome to python programming."
# Check if the string starts with "Hello"
starts_with_hello = test_str.startswith("Hello")    #hello will return False
print("Starts with 'Hello':", starts_with_hello)
starts_with_helloji = test_str.startswith("Helloji")    #hello will return False
print("Starts with 'Helloji':", starts_with_helloji)

# Checks if the string ends with "programming."
ends_with_hello = test_str.endswith("programming.")    #hello will return False
print("Ends with 'programming.':", starts_with_hello)
starts_with_helloji = test_str.endswith("java")    #hello will return False
print("Ends with 'Hello':", ends_with_hello)



# 8. Count() method
#It counts the number of occurences of a substring in the string
# This is case-sensitive
count_str = "Python is great. Python is dynamic. Python is easy to learn"
#count occurences of 'python' 
python_count = count_str.count("python")    #3
print("Occurrences of 'python:", python_count)
#count occurences of 'is' 
is_count = count_str.count("is")    #3
print("Occurrences of 'is:", is_count)
#count occurences of 'java' 
java_count = count_str.count("java")    #0
print("Occurrences of 'java:", java_count)
#count occurences of 's' 
s_count = count_str.count("s")    #3
print("Occurrences of 's:", s_count)


# VVIP
# slicing strings
# slicing allows us to extract a portion of a string using indexing
# last index is not included
# default start is 0 and default end is length of string
# syntax : string_name[start : end]

slice_str = "pythonprogramming"
# Extracting substring from index 0 to 5 (not including 5)
substring1 = slice_str[0:5] # 'pytho'
print("Substring from index 0 to 5: ",substring1)

substring_default_start = slice_str[:6] # 'python'
print("Substring from start to index 6: ",substring_default_start)

substring_default_end = slice_str[6:] # 'programming'
print("Substring from index 6 to end: ",substring_default_end)

substring_default_start_and_end = slice_str[:] # 'python programming'
print("Substring with default start and end: ",substring_default_start_and_end)

#extracting substring using negative indexing
substring2 = slice_str[-4:-1]   # 'min'
print("Substring from index -4 to -1 :", substring2)

# Concatenation
# Concatenation is the process of joining two or more strings into a single string
# It is done using the + operator 
str1 = "Hello"
str2 = "World"
concatenated_str = str1 + " " + str2
print("Concatenated string: ", concatenated_str)

# Repetition
# Repitition is the process of creating a new string by repeating an existing string multiple times
# It is done using the * operator
repeated_str = str1 * 3
print("Repeated string:", repeated_str)

# String with numbers
age = 25
# This will give error : VIMP
# message = "Age is " + age # Error ->Type Error can't add string and int
# print(message)

# Solution 1 : Convert number to string
message = "Age is " + str(age)
print(message)

# Solution 2 : Use comma in print
print("Age is", age)

# Solution 3 : f-strings 
message = f"Age is {age} {30} {25} {str(age)}"
print(message)

name = "Archa"
mobile_number = "1234567890"
# Example: Using f-string to create an email template
email_body = f"""
Hi, {name}
We are conducting a survey for you.
Kindly confirm your mobile number : {mobile_number}
"""
print(email_body)