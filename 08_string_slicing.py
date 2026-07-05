
# Topic : String Slicing
# Description : Accessing a parts of string using slicing 
# Author : Nasir Ali 

#What is String Slicing 
# String slicing is used to extract(نکالنا) a part of string using indexes.

#Basic Slicing 
# str[start : stop : step] # stop index is not included 
word = "Compressor"
print(word[ : ])  # all characters 
print(word[0:3])  #Com 
print(word[2:7])  #mpres

# Start to End
print(word[0:]) # first to last chars
print(word[2:]) # from idx 2 to last chars 

# Negative Slicing 
my_name = "Nasir"
#"N a  s   i   r"
#-5 -4 -3 -2 -1
print(my_name[-3:]) #sir
print(my_name[:-4]) #N
print(my_name[-4: -1]) #asi

# Step value 
text = "programing"
print(text[0:4:1])  
print(text[1:10: 2]) # step = 2 
print(text[1:10:3])  # step = 3
print(text[1:10:4])  # step= 4
print(text[0::2]) # every second 
print(text[::3])
print(text[::])  # all chars
print(text[::-1]) # reverse string 

# Mini practice 

name = "Nasir Ali"
print(name[0:5])
print(name[:5])
print(name[-3:])
print(name[5:6])  #blank space is also a char
print(name[::-1])
print(name[::2])

# What I learned 

# Basic slicing
# Start index
# End index
# Negative slicing
# Step value
# Reverse string

 # Interview questions?
# 1. What is string slicing?
# 2. What is the difference between indexing and slicing?
# 3. How do you reverse a string using slicing?



