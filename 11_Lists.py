
# Topic : Lists
# Description: Learning the fundamentals of lists in Python 
# Author: Nasir Ali 

# What is a List?
# A list is an ordered, mutable collection that can store multiple items of deferent data types.

# Creating List
my_list = [1,2,3] # List are created using square brackets []
print(my_list)
print(type(my_list)) #<class 'list'>
subjects = ["English", "Mathematics", "Physics"]
numbers = [80, 85, 75]
print(subjects)
print(numbers)

# Empty List
empty_list = []
print(empty_list)

# Different Data Types
data = ["Nasir", 25, 5.9, True]
print(data)

# List Length 
values = [10, 20, 30, 40, 50, 60]
print(len(values))

# List Indexing 
countries = ["Pakistan", "India", "Turkey"]
print(countries[0])
print(countries[1])
print(countries[2])
print(countries[-1])

# Updating List
fruits = [ "mango", "apple", "orange"]
fruits[2] = "banana"
print(fruits)
#List is mutable, so their items can be changed 

# Mixed List 

student = [
       "Nasir",
       True,
       25,
       5.9,
]
print(student)

# Membership Operators

students = ["Nasir", "Jafar", "Asad"]
print("Jafar" in students)
print("Ali" in students)

# Nested List 
numbers = [1,2,3, [4,5,6]]
print(numbers)
letters = [
    ["a","b"],
    ["c","d"]
]
print(letters)

# Mini practice 
word = ["Book", "Room", "Jug", "Glass"]
print(type(word))
print(len(word))
print(word[3])
print("Room" in word)
word[1] = "Cup"
print(word)

# What I Learned 

# Creating Lists
# Different Data Types
# type()
# len()
# List Indexing
# Updating Lists
# Membership
# Nested Lists

# Interview Questions 

# 1. What is a list in Python?
# 2. Why is a list called mutable?
# 3. What is the difference between a list and a string?
# 4. Can a list store different data types?
# 5. How do you access the last element of a list?

# Note:
# Lists are one of the most commonly used data structures in Python.
# They are widely used in data analysis, machine learning, and automation.




