
# Topic: Modules Basics
# Description: Learning how to import and use modules in Python 
# Author: Nasir Ali 

#What is a Module?
#A module is a python file that contains function, variables, or classes which can be reused in other programs.

#اردو: Module ایک Python فائل (.py) ہوتی ہے جس میں Functions، Variables یا Classes ہوتی ہیں تاکہ انہیں دوسرے پروگراموں میں دوبارہ استعمال کیا جا سکے۔

#Why do we used Modules?
#Module help us:
#	
# Reuse code 
# Organize Project 
# Save Time
# Access Built-in Library 

#1. Importing a Module 
import math
print(math.sqrt(25))

#2. Using Multiple Functions

import math
print(math.ceil(6.2))
print(math.floor(5.9))
print(math.factorial(6))

#3. Import Specific Function 
from math import sqrt
print(sqrt(49))

#4. Import Multiple Functions 
from math import sqrt, factorial,ceil
print(sqrt(64))
print(factorial(5))
print(ceil(7.3))

#5. Using Alias

import math as m
print(m.sqrt(81))
print(m.factorial(4))

#6. Import Everything 
from math import *
print(sqrt(36))
print(factorial(7))
print(pi)
# Import all functions from the module.
# Generally not recommended because it can cause name conflicts.

# اردو:
# Module کی تمام چیزیں Import ہو جاتی ہیں۔
# عام طور پر اس کا استعمال نہیں کیا جاتا کیونکہ
# مختلف Functions کے نام آپس میں ٹکرا سکتے ہیں۔


#7. Built-in Modules Examples

import math
import random 
import datetime 

# Mathematics Working 
import math 
print(math.sqrt(25))
print(math.pi)

# Random Values 
print(random.randint(1,10))

# Date and Time
import datetime 
print(datetime.datetime.now())
today = datetime.date.today()
print(today)
current_time = datetime.datetime.now()
print(current_time)


#Mini Practice 

import math 
print(math.sqrt(121))
print(math.pow(2,3))

from math import pow
print(pow(2,5))

import math as m
print(m.pow(3,2))
print(m.factorial(6))

#What I Learned

#Modules
#import
#from import
#import as
#Built-in Modules
#math Module
#random Module
#datetime Module

#Interview Questions

#What is a module?
#Why do we use modules?
#What is the difference between import and from ... import?
#What is an alias?
#Why is import * generally not recommended?

#Modules make Python programs cleaner, reusable, and easier to manage.
# They are heavily used in automation, web development, machine learning, and data analysis.
#Not every function in Python is built-in.
#Some functions belong to modules, so we must import the module before using them.

#اردو:
#Python کے تمام Functions Built-in نہیں ہوتے۔

#کچھ Functions مختلف Modules کے اندر ہوتے ہیں،
#اس لیے پہلے Module کو Import کرنا ضروری ہوتا ہے۔

