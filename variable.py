# Storing string in variable
name = "Archa"
print(name)

# Storing number in variable
num = 25
print(num)

# Case sensitivity
name = "John"
Name = "Jane"
NAME = "Jack"

# All three are DIFFERENT variable
print(name) # John
print(Name) # Jane
print(NAME) # Jack

# Assigning same value to diff variables
a = 2
b = 2
c = 2

a = b = c = 2
print(a)
print(b)
print(c)

# Assign multiple values to multiple variables
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

# Assign different data type values to multiple variables
name, age, email = "Archa", 25, "archa@gmail.com"
print(name)
print(age)
print(email)