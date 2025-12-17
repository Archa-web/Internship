
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
starts_with_hello = test_str.startswith("hello")    #hello will return False
print("Starts with 'Hello':", starts_with_hello)
starts_with_helloji = test_str.startswith("Helloji")    #Helloji will return False
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
# Example: Using f-string to create an email template ho
email_body = f"""
Hi, {name}
We are conducting a survey for you.
Kindly confirm your mobile number : {mobile_number}
"""
print(email_body)