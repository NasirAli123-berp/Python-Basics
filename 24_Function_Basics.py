
#Topic: Function Basics
#Description: Learning the fundamentals of functions in Python 
#Author: Nasir Ali 

#What is a Function?
#A function is a reusable block of code that performs a specific task.

#Function کوڈ کا ایسا حصہ ہوتا ہے جو ایک خاص کام انجام دیتا ہے۔
#اور اسے بار بار استعمال کیا جا سکتا ہے ۔

#Why do we use Functions?
#1.Reuse Code 
#2.Reduce Repetition 
#3.Improve Readability 
#4.Easier Maintenance 

#Basic Syntax 

def function_name():
	print("Hello")
	
function_name()

#Simple Example 
def welcome():
    print("Welcome to Python")
welcome()

#Multiple Calls
def hello():
    print("Welcome to the Python by Nasir")
hello()
hello()
hello()

#Function with Calculation
def add_numbers():
	print(2+8)
add_numbers()

#Function with variables 
a = 5
b = 6
def product():
	print(a*b)
	
product()

#Function Returning Nothing 
def message():
	print("Love you Chat GPT")
message()
print(message())
# If a function does not have a return statement, it returns None by default

#Mini Practice 
def my_name():
	print("Nasir")
my_name()

def square():
	print(5**2)
square()

def line():
	print("-"*25)
line()

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def calculations():
	print(a+b)
	print(b-a)
	print(a*b)
	print(a/b)
calculations()


my_list = [1,2,3,4,5]
def my_list_is():
	print(my_list)
	print(len(my_list))

my_list_is()

#What I learned
 
# def keyword
# Function definition
# Function calling
# Reusable code
# Multiple function calls
# Function execution
# None (without return)

#Interview Questions 

#1. What is a function?
#2. Why do we use functions?
#3. What is the purpose of def?
#4. What is function calling?
#5. What happens if a function has no return statement?

#Note:
#Functions are one of the most important concepts in Python.
#They help organize code, reduce repetition,and improve readability.
#Functions are widely used in automation,
#data analysis, web development, and machine learning.
