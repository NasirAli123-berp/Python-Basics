
# Topic: For Loops 
# Description: Learning to repeat tasks using for loops in Python.
#Author: Nasir Ali 

# What is a For Loop?
# A for loop is used to iterate over a sequence
# such as a string, list, tuple, set, dictionary, or range.

# Basic For Loop 
language = "Python" # sequence 

for char in language:
	print(char)
	
# Loop Through String 
word = "Compressor"
for char in word:
	print(char)
# Loop Through List 
my_books = ["Computer","English","Mathematics"]
for book in my_books:
	print(book)
# Loop Through Tuple 
letters = ("a","b","c","d","e")
for char in letters:
	print(char)
# Loop Through Set 
numbers = {1,2,2,3,3,3,4,5}
for num in numbers:
	print(num)
# Loop Through Dictionary 
data = {
    "name":"Ali",
    "age":25,
    "city":"Multan"
}
for key in data:
	print(key)
	
for value in data.values(): 
	print(value)

for key, value in data.items():
	print(key, value)
	
# range(stop)
for i in range(5):
	print(i)

# range(start,stop)

for i in range(2,10): 
	print(i)
	
# range(start,stop,step)

for i in range(1,11,2):  # odd number 
	print(i)
	
for i in range(2,11,2): # even number
	print(i)
for i in range(10,0,-1): 
	print(i)
	
# for Loop with else 
for i in range(3,12):
	print(i)
else:
	print("for loop ended")
	
# Sum Example 
numbers = [5,10,15,20,25,30]
total = 0
for num in numbers:
	total += num
print(total)

total = 0
for i in range(11):
	total += i
print(total)

# Creating Table 
num = int(input("Enter a number: "))
for i in range(1,11):
	print(num,"x",i,"=",i*num)

#Nested Loop 

for i in range(5):
    for j in range(3):
        print(i,j)

# enumerate()
fruits = ["Mango","Apple","Banana","Orange"]

for index,value in enumerate(fruits):
    print(index,value)
    
# Mini Practice 
numbers = (10,20,30,40,50)
for num in numbers:
	print(num)
	
product = 1
for num in numbers:
	product *= num
print(product)

for i in range(11,21):
	print(i)
	
	
# What I learned 

# for loop 
# Loop through String
# Loop through List
# Loop through Tuple
# Loop through Set
# Loop through Dictionary	
# range()
# range(start, stop)
# range(start, stop, step)
# for Loop with else 
# Nested Loop
# enumerate()

# Interview Questions 

#1. What is a for loop?
# 2. What is range()?
# 3. What is the difference between range(5) and range(1,5)?
# 4. How do you loop through a dictionary?
# 5. What is enumerate()?
# 6. What is a nested loop?
# 7. When do we use a for loop?

# Note:
# For loops are one of the most important
# programming concepts in Python.
# They are widely used in automation,
# data analysis, machine learning,
# and data processing.

