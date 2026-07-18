
#Topic: Function Arguments 
#Description: Learning different types of arguments used while calling function in Python.
#Author: Nasir Ali 

#What are Arguments?
#Arguments are the actual values passed to a function when it is called.

#Positional Arguments 
def student(name,age):
	print(name)
	print(age)
student("Nasir",25)

# Keyword Arguments
def student(name,age):
	print(name)
	print(age)
student(name = "Nasir", age = 25)

#Default Arguments
def country(name, city = "Multan"):
	print(name)
	print(city)
country("Nasir")
country("Ali", city= "Lahore")

#Arbitrary Arguments 
def num(*values):
	print(values)
num(10,20,30,40)

# Keyword Arbitrary Arguments 
def student(**data):
	print(data)
student(name= "Nasir",age= 25, city= "Multan")

# Mixing Arguments 

def info(name,age= 24):
	print(name)
	print(age)
info("Nasir")
info("Ali",25)

# Mini Practice 

def add(a,b):
	print(a+b)
add(2,4)

def employee(name, salary):
	print(name)
	print(salary)
employee("Nasir",50000)

def fruits(*items):
	print(items)
fruits("apple","mango","banana")

def student(**data):
	print(data)
student(name= "Nasir",age= 25, height = 5.9)

#Note:
#English: Arguments provide data to functions. Python supports positional, #keyword, default, arbitrary (*args), and keyword arbitrary (**kwargs) arguments