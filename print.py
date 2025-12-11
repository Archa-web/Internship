# print using double quotes and single quotes
print("This is our first program in Python using double quotes") # double quotes 

print('This is our first program in Python using single quotes') # single quotes

# print strings with quotes inside
print("He said, 'Python is awesome!'")
print('She repiled,"Indeed it is!"')

# print numbers(no need for quotes)
print(42)
print(23)

# print multiple items
print("The answer is", 42) # ,(comma) =>  default separator and default value is space
print("Sum of", 20, "and", 22, "is", 42)
print("My", "name", "is", "archa")
print(21,45,2,78)

# print with custom separator
# sep => To add sep by our own
# we can use any string as separator
# we can use single quotes or double quotes for sep value
print("Archa","loves","coding", sep="-")
print(22, 23, 24, sep=":::")

# printing without new line
# end => To add end by our own
# we can use single quotes or double quotes for end value
# we can use any string as end value
print("Hello", end=" ")
print("World") # Both print on same line

# Empty print (creates balnk line)
print()
print("--------------------")

# print using 
print("Hello\nArcha") # \n creates new line
print("Hello\tArcha") # \t creates tab space