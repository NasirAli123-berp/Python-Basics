# Topic : User Input
# Description : Taking input from the user using the input() function 
# Author : Nasir Ali

# What is User Input?
# User input allows the user to enter data while the program is running 
# In Python, the input() function is used to take input from the user 

# Examples 
name = input("enter your name: ")
print(name)

# Input is always a string
age = input("enter your age: ")
print(age)
print(type(age))
# output
# 25
# <class 'str'>

# Integer input 
marks = int(input("enter your marks: "))
print(marks)
print(type(marks))

# Float input 
price = float(input("enter price "))
print(price)
print(type(price))

# Sum of 2 numbers 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1+num2
print("result", sum)

# Mini practice 
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
print("My name is", name, "my age is", age, "my height is", height)
#use f
print(f"My name is { name} my age is {age} my height is {height}")




# What I learned 
# input()
# Taking input from the user 
# input() return always a string 
# int(input())
# float(input())

#Note
#The input() function  always returns a string 
# Use int() and float() when numeric input is required 




