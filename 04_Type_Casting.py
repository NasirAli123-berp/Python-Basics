#Topic : Type Casting 
#Description : Converting one data type into another 
#Author : Nasir Ali

#What is Type Casting 
#Type Casting is used to convert one data type into another 

# Integer to Float
num = 8
result = float(num) # float( ) add the decimal part
print(result)
print(type(result))
# output
# 8.0
# <class 'float'>

# Float to Integer
price = 77.89
result = int(price)
print(result)
print(type(result))
# output
# 77
# <class 'int'>
# int( ) remove the decimal part

# Integer to String
age = 25
text= str(age)
print(text)
print(type(text))

# String to Integer
number = "50"
value = int(number)
print(value)
print(type(value))

# String to Float
height = "5.9"
value = float(height)
print(value)
print(type(value))

# Boolean Casting 
print(bool(1))
print(bool(0))
print(bool("Nasir"))
print(bool(""))

# Wrong type casting 
# This will cause an error 
# num = "Ali"
# print(int(num))


#Mini Practice 
marks = "90"
my_marks = int(marks)
percentage = float (marks)
print(my_marks)
print(percentage)
print(type(my_marks))
print(type(percentage))


#what i learned 

# int( )
# float( )
# str( )
# bool( )
# safe type conversion 


