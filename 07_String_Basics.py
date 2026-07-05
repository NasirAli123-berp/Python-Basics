
# Topic : String Basics
# Description : Learning the fundamentals of Strings in Python 
# Author : Nasir Ali 

# What is a String 
#A string is a sequence(ترتیب) of characters(حروف) enclosed in single, double or triple quotes.

# Single quote 
name = 'Nasir'
print(name)

# Double quote 
city = "Multan"
print(city)

# Triple quotes 
message = """ Welcome to Python"""
print(message)

# type()
text = "Python"
print(type(text))

# Concatenation 
first = "hello"
last = "world"
print(first + last)  #-----> 'hellowould'
print(first + " " + last) #add space ('hello world')

# Length of String
language = "Python"
print(len(language)) #len() is Python function

# String Indexing 
str= "Nasir_Ali"
#N a s  i  r _ A  l  i
#0 1 2 3 4 5 6 7 8
#str[0] is 'N'  ,str[1] is 'a'

print(str[0])
print(str[1])
print(str[5])
print(str[-1])

#String Repetition
print("python" * 3 )

#String Membership 
text = "Python"
print("P" in text)
print("h" in text)
print("j" in text)

# Mini practice 
name = "Nasir"
country = "Pakistan"
print(name)
print(country)
print(type(name))
print(len(name))
print(name[0])
print(name[-1])
print(name + " " + country)
print("N" in name)

# ===================
# What I Learned
# ===================

# What is a string
# Single quotes
# Double quotes
# Triple quotes
#type()
# String indexing
# len()
# Concatenation
# Repetition
# Membership

# Note:
# Strings are one of the most commonly used data types in Python.
# They are widely used in data analysis, web development, automation, and machine learning.

# ===================
# Interview Questions
# ===================

# 1. What is a string?
# 2. What is string indexing?
# 3. What is the difference between positive and negative indexing?
# 4. What does len() do?
# 5. How do you join two strings?

