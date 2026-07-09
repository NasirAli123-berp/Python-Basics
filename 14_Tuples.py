
# Topic: Tuples 
# Description: Learning the fundamentals of tuples in Python 
#Author: Nasir Ali 

#What is a Tuple?
# A tuple is an ordered and immutable collection
#that can store multiple items of different data types 

# Creating Tuple 
my_tup = ()
print(type(my_tup))

numbers = (10,20,30,50,70,100)
print(numbers)

# Different Data Types 
my_data = ("Nasir",25,5.9, True)
print(my_data)
# Tuple Length 
print(len(my_data))

# Indexing 
subjects = ("Eng","Math","Phy","Bio","Urdu")
print(subjects[0])
print(subjects[2])
print(subjects[-1])
# Slicing 
print(subjects[:])
print(subjects[2:])
print(subjects[1:3])
print(subjects[-4:-1])
print(subjects[::2])
print(subjects[1:3:1])
print(subjects[::-1])

# Membership 
print("Math" in subjects)
print("Comp" in subjects)

# Nested Tuple
data = ((2,3,4),(5,6,7))
print(data)
print(data[0])
print(data[1][0])

# One Item Tuple 
fruit = ("apple",)
print(type(fruit)) # <class 'tuple'>
fruit = ("apple")
print(type(fruit))# <class 'str'>

# Immutable Example 
numbers = (10,20,30)
#numbers[0] = 50
#Type error 

# Packing and Unpacking 
person = ("Nasir",25,"Multan")
name,age,city = person 
print(name)
print(age)
print(city)

#Mini Practice 
student = ("Nasir",25,5.9,"Multan", True )
print(student)
print(type(student))
print(len(student))
print(student[0])
print(student[-1])
print(student[3:])
print(student[1:4:2])
print(student[-4::])
print("Multan" in student)

# What I learned 
# Creating Tuples
# Different Data Types
# type()
# len()
# Tuple Indexing
# Tuple Slicing
# Membership
# Nested Tuples
# One Item Tuple
# Packing and Unpacking
# Immutable Tuples

# Interview Questions 

# 1. What is a tuple?

# 2. What is the difference between a list and a tuple?

# 3. Why are tuples immutable?

# 4. How do you create a tuple with one item?

# 5. What is tuple unpacking?

# Note:
# Tuples are commonly used to store fixed data.
# They are faster than lists and help protect data
# from accidental modification.
# Tuples are often used when data should not be changed.




