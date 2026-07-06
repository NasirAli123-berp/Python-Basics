
# Topic : String Formatting 
# Description: Formatting strings in deferent ways in Python 
# Author: Nasir Ali 

#What is String Formatting?
# String formatting is used to insert variables and values into a string.

#String Concatenation 
name1 = "Nasir"
name2 = "Ali"
print(name1 + " " + name2)

# Old Style Formatting 
name = "Nasir"
age = 25
print("My name is %s." % name)
print("I am %d years old." % age)

# .format() Methods 

name = "Nasir"
city = "Multan"

print("My name is {}.".format(name))
print("I live in {}.".format(city))
print("My name is {} and I live in {}.".format(name, city))

# f-Strings ⭐
name = "Nasir"
age = 25
height = 5.9
city = "Mutan"
print(f"my name is {name} I am {age} year old my height is {height} I live in {city}")

# Expressions in f-Strings 
x = 15
y = 25

print(f"sum = {x+y}")
print(f"subtract = {x-y}, product = {x*y}, division = {y/x}")

# Escape Characters 
print("my name is Nasir \n.l live in Multan") # New line

print("hello\tworld") # Tab space 

print("He said,\"Python is awesome!\"")


print(" \"kw-double Quotes\" ")  # double quotes using \

print(" \'kw-single Quotes\' ") # single quote using \

#Mini practice 
name = "Nasir"
age = 20
course = "Python"
marks = 95

print(f"My name is {name}.")
print(f"I am learning {course}.")
print(f"My marks are {marks}.")
print(f"Next year I want to learn Data Analysis.")
print(f"My name is {name} and I'm {age}")
print(f"My age after 5 years will be {age + 5}")
 
# What I learned 

# String Concatenation
# % Formatting
# .format()
# f-strings
# Escape Characters

# Interview Questions 

# 1. What is string formatting?
# 2. What is the difference between .format() and f-strings?
# 3. Which string formatting method is recommended in modern Python?
# 4. What is the purpose of escape characters?

#Note

# Note:
# f-strings are the most recommended and widely used
# string formatting method in modern Python because
# they are simple, readable, and fast.
