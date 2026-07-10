
# Topic: Tuple Methods 
# Description: Learning the built-in methods and functions of tuples in Python 
# Author: Nasir Ali 

# What are Tuple Methods 
# Tuple methods are built-in methods used to work with tuples
# Since tuples are immutable, they have only two built-in methods.

#1. Count()
numbers = (10,20,30,20,10,30,20)
print(numbers.count(20))
print(numbers.count(50))

#2. index()
subjects = ("English","Mathematics","Physics","Computer")
print(subjects.index("Physics"))
print(subjects.index("English"))

# Useful Built-in functions 

#3. len()
numbers = (5,10,15,20,25,30,35)
print(len(numbers))
#4. sum()
print(sum(numbers))
#5. max()
print(max(numbers))
#6. min()
print(min(numbers))

# Mini practice 
numbers = (2,4,6,2,7,4,8,9,2,3,2)
print(numbers.count(2))
print(numbers.index(4)) # show first index in tuples 
print(len(numbers))
print(sum(numbers))
print(max(numbers))
print(min(numbers))

# What I learned 
# count()
# index()
# len()
# max()
# min()
# sum()

# Interview Questions 
# 1. How many built-in methods does a tuple have?

# 2. Why does a tuple have fewer methods than a list?

# 3. What is the difference between count() and index()?

# 4. Which function returns the largest value in a tuple?

# 5. Which function returns the total of all numbers in a tuple?

# Note:
# Tuples have only two built-in methods because they are immutable.
# Functions like len(), max(), min(), and sum() are commonly used with tuples.
