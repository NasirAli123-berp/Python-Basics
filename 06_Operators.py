# Topic : Operators
# Description : Performing defferent operations using python operator 
# Author : Nasir Ali 

# What are Operators?
#Operators are special symbols used to perform operations on variables and values.

# 1. Arithmetic Operators 
# These Operators are used to perform mathematical calculations
# +, -, *, /, %, //, **
a = 10
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

# 2. Assignment Operators
# These Operators are used to assign values to variables.
# +=, -=, *=, /=, %=, //=, **=

x = 10
x += 5 # x = x + 5
print(x)
a = 7
a -= 3 # a = a - 3
print(a)
b = 4
b *= 7 #b = b * 7
print(b)
c = 8
c /= 4 # c = c /b4
print(c)
d = 12
d %= 8 # d = d % 8
print(d)
e = 16
e //= 6 # e = e // 6
print(e)
f = 4
f **= 2 # f = f ** 3
print(f)

# 3. Comparison Operators
# Comparison Operators used to compare two values.
# ==, !=, >, <, >=, <=, 
                           #output
print(20==20)  #True
print(10!=15)   #True
print(5>3)       #True
print(10<12)   #True
print(10>=10) #True
print(8<=5)     #False

# 4. Logical Operators
#Logical operators used to combine conditional statement.
# and, or, not

print(True and True)  #True
print(True and False) #False
print(True or False)  #True
print(not True )    # False 

# 5. Identity Operators 
# Used to check whether two variables refer to the same object.
# is, is not

m = [1,2,3]
n = m
o = [1,2,3]
print(m is n)  #True
print(m is o)  #False
print(m is not o)  #True

# 6. Membership Operator 
# Used to chack whether a value exists in a sequence.
# in, not in

fruits = ["apple", "mango","banana"]
print("apple" in fruits)  # True
print("orange" in fruits) # False
print("orange" not in fruits) #True

#Mini practice 
x = 10
y = 5
print(x+y)
print(x!=y)
print(x>y)
print(x%y)
print(x==y)
print(x//y)

# ==================
# What I Learned
# ==================

# Arithmetic Operators
# Assignment Operators
# Comparison Operators
# Logical Operators
# Identity Operators
# Membership Operators

#Note
#Operators are  one of the most important concept in Python 
# They are used in calculations, conditions, loops and functions.

# =====================
# Interview Questions
# =====================

# 1. What are operators in Python?
# 2. What is the difference between == and is?
# 3. What is the difference between / and // ?

