
# Topic: While Loops 
# Description: Learning to repeat tasks using while loops in Python.
#Author: Nasir Ali 

# What is a While Loop?
# A while loop repeatedly executes a block of 
# code as long as the given condition is True.
# while loop اس وقت تک بار بار کوڈ چلاتی ہے
# جب تک دی گئی condition True رہے۔

# Basic While Loop 
i = 1
while i <= 5:
	print(i)
	i += 1
num = 1
while num <= 3:
	print("Nasir")
	num += 1
# Counting Example 
num = 10
while num >= 1:
	print(num)
	num -= 1
else:
	print("end")
# Sum Example
i = 1
total = 0
while i <= 5:
	total += i
	i += 1
print(total)

#Multiplication Example 
num= int(input("Enter a number: "))
i = 1
while i <= 10:
    print(num, "x", i, "=", num* i)
    i += 1

# Even Numbers
i = 2
while i <= 20:
	print(i)
	i += 2
	
# Odd Numbers 
i = 1
while i <= 10:
	print(i)
	i += 2

# while with else 
i = 1
while i <= 8:
	print(i)
	i += 1
else:
	print("loop, ended")
	
# Infinite Loop 
#while True:
#	print("Hello")

# User Input Example 
password = ""
while password != "nasir123":
    password = input("Enter password: ")
print("Access Granted")

# Mini Practice 
i = 1
while i <= 4:
	print(i)
	i += 1
i = 1
while i < 4:
	print(f"Hello Nasir{i}", sep = "")
	i += 1
else:
	print("end")
i = 1
while i < 4:
	print(f" Hello{i}","Nasir", sep = "*",end =" ")
	i += 1
	
# What I learned 
# while loop
# Condition
# Counter
# Even Numbers 
# Odd numbers 
# while-else
# Infinite Loop
# User Input Loop

# Common Mistakes

# 1. Forgetting to update the counter
# This can create an infinite loop.
# 2. Wrong indentation
# 3. Incorrect loop condition

# Interview Questions 

# 1. What is a while loop?
# 2. What is the difference between for and while loops?
# 3. What happens if the condition never becomes False?
# 4. What is an infinite loop?
# 5. What is while-else?
# 6. Why is increment important in a while loop?
# 7. When should you use a while loop instead of a for loop?

# Note:
# While loops are useful when the number of
# iterations is unknown.
# They are widely used in automation,
# games, user input validation,
# and real-world applications.

