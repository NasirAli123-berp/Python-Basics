
# Topic : List Methods 
# Description: Using built-in methods to modify and manage  lists in Python 
# Author: Nasir Ali 

# What is a List Methods?
# List Methods are built-in functions used to add, remove, update or organize items in a list.

#1. append()
subjects = ["English", "Mathematics", "Physics"]
subjects.append("Chemistry") #adds one item at the end
print(subjects)

#2. extend()
fruits = ["banana", "orange"]
fruits.extend(["mango", "apple"])
print(fruits)
more_fruits = ["cherry", "grapes"] #anaother list 
fruits.extend(more_fruits)
print(fruits)

#3. insert()
fruits = ["banana", "orange"]
fruits.insert(0, "apple") # Insert at index 0
fruits.insert(1, "mango")
print(fruits)

#4. remove()
subjects = ["English", "Mathematics", "Physics"]
subjects.remove("Physics")
print(subjects)

#5. pop()
numbers =[5,10,15,20]
numbers.pop() # delete last item
print(numbers)

numbers.pop(0)
print(numbers)

#6. clear()
nums = [2,4,6,8]
nums.clear()
print(nums)

#7. index()
fruits = ["banana", "orange", "grapes", "banana"]
print(fruits.index("orange"))
print(fruits.index("banana", 2)) # finding idx- within a range 

#8. count()
numbers = [10,20,30,30,30,40,40]
print(numbers.count(20))  # 1
print(numbers.count(30))  # 3
print(numbers.count(5)) #  0

#9. sort()
numbers = [7,3,4,6,2,1,5]
numbers.sort() # default sort ascending order
print(numbers)
numbers.sort(reverse = True)
print(numbers)
# Strig sorting 
fruits = ["cherry", "apple", "banana"]
fruits.sort()
print(fruits)
fruits.sort(key=len, reverse=True)
print(fruits)

#10. reverse()
nums = [5,4,3,2,1]
nums.reverse()
print(nums)

#.11 copy()
numbers = [1,3,5,7]
new_numbers = numbers.copy()
print(new_numbers)

#================
#Mini practice 
#================
countries =["Pakistan", "Turkey", "India"]
countries.append("Qatar")
print(countries)
countries.remove("India")
print(countries)
print(countries.index("Turkey"))
countries.pop()
print(countries)
countries.clear()
print(countries)

#What I learned 
# append() ہمیشہ آخر میں ایک نئی Value شامل کرتا ہے۔
# extend()  ایک وقت میں متعدد Items شامل کرتا ہے۔
# insert() insert(index, value) کسی خاص جگہ پر نئی Value شامل کرتا ہے۔
# remove()  Value کے نام سے Item حذف کرتا ہے۔
# pop() آخری Item حذف کرتا ہے۔
# clear()   پوری List کو خالی کر دیتا ہے۔
# index() کسی Value کا Index بتاتا ہے۔
# count()  بتاتا ہے کہ کوئی Value کتنی بار موجود ہے۔
# sort() List کو چھوٹے سے بڑے نمبر کی ترتیب میں لگا دیتا ہے۔
# reverse() پوری List کو الٹ دیتا ہے۔
# copy() List کی نئی Copy بناتا ہے۔

# Interview Questions 

# 1. What is the difference between append() and extend()?
# 2. What is the difference between remove() and pop()?
# 3. Which method is used to sort a list?
# 4. How do you copy a list?
# 5. Which method removes all items from a list?

# Note:
# List methods are widely used in data analysis for cleaning,
# updating, sorting, and organizing data before analysis.
