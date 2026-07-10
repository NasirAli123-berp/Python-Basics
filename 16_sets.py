
# Topic: Sets
# Description: Learning the fundamentals of sets in Python 
# Author: Nasir Ali 

# What is a Set?
# A set is an unordered and mutable collection of unique items.

# Creating sets

numbers = {1,2,3,4}
print(numbers)
print(type(numbers))

# Empty set
null_set = set() 
print(null_set)
print(type(null_set)) #<class 'set'>

my_set = {}
print(type(my_set)) # <class 'dict'>
# This is not a set

# Different Data Types 

data = {"Nasir",25,5.9, True }
print(data)

# len()
numbers = {1,3,5,6,7,8,9,11}
print(len(numbers))

# Membership 
fruits = {"apple","mango", "orange"}
print("mango" in fruits)

# Duplicate values
nums = {1,2,2,3,5,4,4,4,2,3,5}
print(nums)
# repeated elements stored only once, so it resolved to {1,2,3,4,5}
# Duplicate values are automatically removed.

# Unordered Nature 
colors = {"Red","Blue","Green"}
print(colors)
# Add Example
colors.add("White")
print(colors)
# Remove 
colors.remove("Red")
print(colors)

#Mini Practice 
numbers = {1,2,2,3,5,6,4,7,8,9,11}
print(numbers)
print(type(numbers))
print(len(numbers))

# What I learned 
# Creating Sets 
# Empty Set
# Type of Sets 
# Different Data Types 
# len()
# Membership 
# Duplicate values 
# Unordered Nature 

# Interview Questions 
# 1. What is a set?
# 2. Why are duplicate values removed in a set?
# 3. What is the difference between a list and a set?
# 4. How do you create an empty set?
# 5. Why is a set unordered?

# Note:
# Sets are useful for storing unique values.
# They are commonly used in data cleaning,
# removing duplicates, and membership testing.