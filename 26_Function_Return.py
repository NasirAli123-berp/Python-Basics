#Topic: Function Return 
#Description: Learning how functions return values using the return statement.
#Author: Nasir Ali

#What is Return?
#The return statement sends a value back from a function.
#اردو: return Function کے اندر سے حاصل ہونے والا Result واپس بھیجتا ہے تاکہ بعد میں اسے استعمال کیا جا سکے۔

# Simple Return 
def hello():
	return "Hello"
print(hello())

# Returning Number 
def add():
	return 7+15
print(add())

# Return with Variables 
def subtract():
	a = 50
	b = 30
	return a-b
print(subtract())

# Return with Parameters 
def multiply(a,b):
	return a*b
print(multiply(6,8))

# Store Return Values
def add(num):
	return num + 10
result = add(20)
print(result)

# Return String 
def fullname(first, second):
	return first+" "+second
result = fullname("Nasir","Ali")
print(result)

# Return List
def my_list(data):
	return data 
result = my_list(["apple","mango", "banana" ])
print(result)
# Return Dictionary 
def subjects(marks):
	return marks
result = subjects({
    "Computer":99,
    "English":95,
    "Mathematics":97
})
print(result)

# Return Boolean 
def is_even(num):
	return num % 2 == 0
print(is_even(8))
print(is_even(3))

#Multiple Return (Tuples)
def calculations(a,b):
	return a+b,a-b,a*b
print(calculations(15,7))
add, sub, mul = calculations(10,5)
print(add)
print(sub)
print(mul)

# Return ends Function 
def message():
	print("Hello")
	return
	print("Nasir")
message()

# return inside if
def check(age):
	if age >= 18:
		return "adult"
	return "minor"
print(check(20))



# Mini Practice 
def hello():
	return "Welcome to the Python"
print(hello())

def square(num):
	return num **2
result = square(5)
print(result)

def cube(num):
	return num **3
print(cube(6))

def average(num):
	return sum(num) / len(num)
result = average((10,20,30,40,50))
print(result)

def check_even_odd(num):
	if num %2 == 0:
		return "Even"
	return "Odd"
result = check_even_odd(int(input("Enter a number: ")))
print(result)

def full_name(first,last):
	return first + " " + last 
print(full_name("Jafar","Ali"))

def area_rectangular(length,width):
	return length * width 
result = area_rectangular(70,50)
print(result)

def celsius_to_fahrenheit(celsius):
	fahrenheit = (celsius*9/5)+32
	return fahrenheit 
temp_fah = celsius_to_fahrenheit(25)
print(temp_fah)

# What I learned 

#return statement
#Returning values
#Returning numbers
#Returning strings
#Returning lists
#Returning dictionaries
#Returning Boolean values
#Multiple return values
#Tuple unpacking
#return with if
#return ends function

#Interview Questions
#What is the purpose of the return statement?
#What is the difference between print() and return()?
#Can a function return multiple values?
#What happens after a return statement is executed?
#Can a function return a list or dictionary?





	