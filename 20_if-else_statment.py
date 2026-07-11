
#Topic: If-Else Statement 
#Description: Learning decision-making using if, elif and else in Python 
#Author: Nasir Ali 

#What is an If Statement 
# An if statement is used to make decisions based on conditions.

# if-elif-else Syntax 
#if(condition):
#	statement1
#elif(condition):
#	statement2
#else:
#	statementN

# Simple if Statement 
is_student = True
if is_student: # if Statement works for only True condition 
	print("True")
	
marks = 70
if marks >= 50:  #True
	print("Student is pass")

a = 10
b = 25
if a <= b:  #True
	print("b is greater than a")

# if-else Statement

a = 5
b = 10
if a >= b:  # False --> no output 
	print("a is greater than b")
else:
	print("b is greater than a ")
#else statement handles False conditions 
age = int(input("enter your age: "))
if age >= 19:
	print("You are an adult")
else:
	print("You are not an adult")

# if-elif-else Statement 
# check multiple conditions 
marks = 80
if marks >= 90:
	print("Grade A")
elif marks >= 80:
	print("Grade B")
elif marks >= 60:
	print("Grade C")
else:
	print("Grade D")

data = ["Nasir",25,5.9,"Multan"]
if len(data) == 3:
	print("3 is True")
elif len(data) == 2:
	print("2 is True")
elif len(data) == 4:
	print("4 is True")
else:
	print("False")

#Multiple Conditions 
#(and,or)
age = 25
city = "Multan"
if age >=18 and city == "Multan":
	print("Eligible")
my_str = "Welcome Python"
if my_str[0] == "W" and my_str[1:6] == "elcom":
	print("True")
# or
if my_str.endswith("hon") or my_str.count("o") == 4:
	print(True)
	
# not
logged_in = False
if not logged_in:
    print("Please login first.")

# Nested if
age = 25
if age >= 18:
	if age >=23:
		print("adult")
		
numbers = int(input("Enter a number: "))
if numbers > 0: # chacking positive number
	if numbers %2 == 0:
		print("This is an even number")
	else:
		print("This is an odd number")
else:
	if numbers == 0:  # chacking zero value
		print("This is zero")
	else:
		print("This is a nagetive number")
		
# Short hand if
marks = 55 
if marks >= 50: print("Pass")

#Short-hand if-else 
#(Ternary Operators)
age = 16
print("Adult") if age >= 18 else print("Minor")

# Mini Practice 
a = 5
b = 15
c = 10
if a < b:
	print("b is greater than a")
if a >= b and b >= c:
	print("a, greatest")
elif b >= a and b >= c:
	print("b, greatest")
else:
	print("c, greatest")

if a > b or b > c:
	print("b greater than a and c")

#What I learned 
#if-elif-else syntax 
# if statement
# if-else
# if-elif-else
# Nested if
# and
# or
# not
# Short-hand if
# Short-hand if-else

#Interview Questions 

# 1. What is an if statement?
# 2. What is the difference between if and if-else?
# 3. When do we use elif?
# 4. What is a nested if statement?
# 5. What is the difference between and and or?
# 6. What is the purpose of not?
# 7. What is a ternary operator?

# Note:
# If-Else statements are one of the most important
# control structures in Python.
# They are widely used in automation,
# data analysis, machine learning,
# and real-world applications.
# Conditional statements control the flow
# of a Python program.

	
	