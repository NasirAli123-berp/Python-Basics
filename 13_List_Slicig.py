
# Topic : List Slicing 
# Description: Accessing  parts of a list using slicing in Python
# Author: Nasir Ali 

# What is  List Slicing?
# List slicing is used to extract a portion of a list using indexes.

# Slicing Syntax 
# list_name[start: stop: step]


my_list = [10,20,30,50,70,80,100]
# index:   0   1   2   3   4   5   6  
# index:  -7  -6  -5  -4  -3  -2  -1

# Basic Slicing 

numbers = [5,10,15,20,25]

print(numbers[:]) # Complete list 
print(numbers[0:3])
print(numbers[1:4])
print(numbers[0:2])

# Start to End 
letters = ["a","b","c","d"]

print(letters[0:])
print(letters[2:])

# Beginning to Specific Index 
print(letters[:2])
print(letters[:3])

# Negative Slicing 
nums = [4,8,12,16,20]
print(nums[-1:])
print(nums[-4:-1])
print(nums[:-3])

# Step value 
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[::])
print(numbers[::2])
print(numbers[1::2])
print(numbers[1:8:3])
print(numbers[3:7:1])

# Reverse List
print(numbers[::-1])

# Copy a List
new_numbers = numbers[:]
print(numbers)
print(new_numbers)
#Nested List Slicing 
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0])
print(matrix[1])
print(matrix[0][2])

# Mini Practice 
subjects = ["Eng", "Math","Phy","Bio"]
print(subjects[:])
print(subjects[2:])
print(subjects[:3])
print(subjects[-2:])
print(subjects[::3])
print(subjects[1:2:2])
print(subjects[::-1])

# What I learned 
# List Slicing Syntax 
# Basic Slicing 
# Nagetive Slicing 
# Step Value 
# Reverse List
# Copy List 

# Interview Questions 
# 1. What is list slicing?
# 2. What is the difference between indexing and slicing?
# 3. How do you reverse a list using slicing?
# 4. How do you copy a list using slicing?
# 5. What is the purpose of the step value?

# Note:
# List slicing is widely used in data analysis to select,
# filter, and process specific parts of datasets.
# Slicing helps work with specific parts of large datasets efficiently.
