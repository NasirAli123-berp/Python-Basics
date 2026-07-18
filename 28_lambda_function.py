
#Topic: Lambda Function 
#Description: Learning anonymous functions using lambda Expressions in Python 
#Author: Nasir Ali

#What is a Lambda Function?
#A lambda function is a small anonymous function
#used to perform a simple tasks in a single line 

# Lambda Function ایک چھوٹا Function ہوتا ہے
# جس کا کوئی نام (Name) نہیں ہوتا۔
# اسے صرف ایک سادہ کام کے لیے ایک ہی لائن میں لکھا جاتا ہے۔

sum = lambda num: num + 10
print(sum(50))

square = lambda x: x**2
print(square(6))

cube = lambda a : a**3
print(cube(5))

add = lambda a,b: a+b
print(add(50,100))

volume = lambda l,w,h:l*w*h
print(volume(12,20,15))

#Boolean Example 
even = lambda num: num%2== 0
print(even(8))
print(even(5))

#lambda with if-else
check = lambda age: "you can vote" if age >= 18  else "you cannot vote"
print(check(21))
print(check(20))
print(check(15))

#lambda with string 
welcome = lambda name: "Hello" + " " + name
print(welcome("Nasir"))

# lambda with list
numbers = [10,20,30]
double = list(map(lambda x:x*2,numbers))
print(double)

#lambda with sorted()
names = ["Ali","Nasir","Ahmad","Zain"]
print(sorted(names,key=lambda x:len(x)))
# lambda with max()
numbers=[4,8,2,15,9]
print(max(numbers,key=lambda x:x))
# lambda with min()
numbers=[4,8,2,15,9]
print(min(numbers,key=lambda x:x))
print(min(numbers,key= lambda a:a))

#Mini Practice 
square = lambda x:x**2
print(square(7))

cube = lambda x:x**3
print(cube(3))

add = lambda a,b:a+b
print(add(15,20))

rectangular = lambda L,W: L*W
print(rectangular(40,15))

fullname = lambda first,last:first+" "+last
print(fullname("Nasir","Ali"))

check = lambda num:"Even" if num%2==0 else "Odd"
print(check(9))

# What I learned 
# Lambda Functions
# Anonymous Function
# Lambda Syntax
# Single Parameter
# Multiple Parameters
# Lambda with Strings
# Lambda with Numbers
# Lambda with Boolean
# Lambda with if-else
# Lambda with sorted()

# Interview Questions 
# 1. What is a lambda function?
# 2. Why is it called an anonymous function?
# 3. What is the difference between a normal function and a lambda function?
# 4. Can a lambda function have multiple parameters?
# 5. When should we use lambda functions?

#Note:
# Lambda functions are best for short,
# simple, one-line operations.

# اردو:
# Lambda Functions چھوٹے، سادہ اور
# ایک لائن والے کاموں کے لیے بہترین ہوتے ہیں۔
# یہ خاص طور پر Pandas اور Data Analysis میں
# بہت زیادہ استعمال ہوتے ہیں۔


