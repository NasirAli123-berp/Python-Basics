
#Topic: Function Parameters 
#Description: Learning how to pass data to functions using parameters and arguments in Python.
#Author: Nasir Ali 

#What are Parameters?
#Parameters are variables defined inside the function parentheses to receive data.

#Parameters وہ Variables ہوتے ہیں جو Function کے اندر () میں لکھے جاتے ہیں تاکہ باہر سے آنے والی Values کو وصول (Receive) کر سکیں۔

#What are Arguments?
#Arguments are the actual values passed to a function when it is called.

#Arguments وہ اصل Values ہوتی ہیں جو Function کو Call کرتے وقت دی جاتی ہیں۔

#Simple Example 

def greet(name):
	print("Hello",name)
greet("Nasir")

# Single Parameter

def my_subject(book):
	print(book)
my_subject("Computer")
my_subject("English")

# Multiple Parameters 

def data(name,age,height):
	print("My name is",name)
	print(f" I am {age} year old")
	print("My height is", height)
data("Nasir",25,5.9)
data("Ali",22,5.8)

# Addition Example 
def add(a,b):
	print(a+b)
add(20,30)
add(99,1005)

#Different Data Types 

def information(name, age, height, student):
    print(name)
    print(type(name))
    print(age)
    print(type(age))
    print(height)
    print(type(height))
    print(student)
    print(type(student))

information("Nasir", 25, 5.9, True)
information("Sara", 22, 6.1, False)

#String Parameter

def welcome(message):
	print(message)
welcome("Welcome to Python by Nasir")

# List Parameter 
def show_items(items):
	print(items)
	print(type(items))
	print(len(items))
show_items(["Computer","Battery","keyboard"])
# Tuple Parameter 
show_items((10,20,30,40,45))
# Set Parameter
show_items({1,2,2,3,4,4,4,5})

# Dictionary Parameter
def employee(data):
    print(data)
    print(type(data))
employee({
    "name":"Nasir",
    "age":25,
    "city":"Multan"
})

#Function Calling Multiple Times
def welcome(name):
	print("Assalamualaikum", name)
welcome("Nasir")
welcome("Ali")
welcome("Ahmad")
welcome("Sara")

# Mini Practice 

def city(name):
	print("My city", name )
city("Multan")

def calculations(a,b):
	print(a+b)
	print(a-b)
	print(a*b)
	print(a/b)
calculations(9,3)

def square(number):
    print(number ** 2)

square(5)
square(10)
square(20)

#What I learned 

# Parameters
# Arguments
# Single Parameter
# Multiple Parameters
# Passing Numbers
# Passing Strings
# Passing Lists
# Pssing Tuples
# Passing sets
# Passing Dictionaries
# Function Calling

# Interview Questions 

#1. What is a parameter?
#2. What is an argument?
#3. What is the difference between parameters and arguments?
#4. Can a function have multiple parameters?
#5. Can we pass a list to a function?
#6. Can we pass a dictionary to a function?

# Note:
	
#Parameters receive data, while arguments send data to functions.
#اردو
#Parameters ڈیٹا وصول (Receive) کرتے ہیں جبکہ Arguments Function کو ڈیٹا بھیجتے (Send) ہیں۔
