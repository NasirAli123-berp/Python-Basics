
# Topic: Set Methods 
# Description: Learning the built-in methods and operations of sets in Python
# Author: Nasir Ali 

# What  are Set Methods?
# Set methods are built-in functions used to add, remove, update and perform operations on sets.

# Part 1: Basic Methods 
#1. add()
subjects = {"Computer","English ","Mathematics"}
subjects.add("Statistics")
print(subjects)
#2. remove()
subjects.remove("Mathematics")
print(subjects)
#3. update()
subjects.update(["Physics","Chemistry"]) # add multiple values 
print(subjects)
#4. discard()
subjects.discard("Biology") # No error if the item does not exist.
print(subjects)

#5. pop()
colors = {"Red", "Blue", "Green","Yellow"}
colors.pop() # pop() removes a random item.
print(colors)
#6. clear()
colors.clear()
print(colors)

#7. copy()
numbers = {1,2,3,4,6}
new_numbers = numbers.copy()
print(new_numbers)

# Part 2: Sets Operations 

#1. union()
X = {1,2,2,3,3,4}
Y = {2,3,4,4,5,5}
print(X.union(Y))# Duplicate values are removed automatically.
#2. intersection()
print(X.intersection(Y))
#3. difference()
print(X.difference(Y))
#4. symmetric_difference()
print(X.symmetric_difference(Y))

# Mini Practice 
A = {1,2,3}
B = {3,4,5}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))
A.add(6)
print(A)
B.remove(3)
print(B)
B.clear()
print(B)
A.pop()
print(A)
A.update([4,5,6])
print(A)

# What I learned 
# add()
# update()
# remove()
# discard()
# pop()
# clear()
# copy()
# union()
# intersection()
# difference()
# symmetric_difference()

# Interview Questions 
# 1. What is the difference between add() and update()?
# 2. What is the difference between remove() and discard()?
# 3. What does pop() do in a set?
# 4. What is the difference between union() and intersection()?
# 5. When would you use sets in data analysis?

# Note:
# Sets are widely used in data analysis for removing
# duplicates, comparing datasets, and finding unique values.
# Sets are especially useful for removing duplicate values from datasets.