
# Topic : String Methods
# Description : Using built-in string methods to manipulate text in Python 
# Author : Nasir Ali

# What are string methods?
# String Methods are built-in functions used to modify, search and analyze strings.

# String Methods 

word = "Welcome, Nasir"
#1.  len()
print(len(word))
#2.  upper()
print(word.upper()) #Converts all letters to uppercase.
#3.  lower()
print(word.lower()) #Converts all letters to lowercase.
#4.  count()
print(word.count("N")) #Counts how many times a character or word appears in a string.
#5.  find()
print(word.find("s")) #Returns the position (index) of a word or character.
print(word.find("z"))
#6.  split()
print(word.split()) #Converts a string into a list.
print(word.split(","))
#7.  replace()
print(word.replace("Welcome","Hello")) #Replaces one word or character with another.
#8.  title()
word2 = " my name is Nasir "
print(word2.title()) #Capitalizes the first letter of each word.
#9.  capitalize()
print(word.capitalize()) #Capitalizes only the first letter of the first word.
#10.  strip()
text = "  hello world  "
print(len(text)) #Removes extra spaces from the beginning and end of a string.
print(text.strip())
print(len(text.strip()))
#11.  join()
fruits = ["apple", "orange", "mango"]
print(", ".join(fruits)) #Converts a list back into a string.
print(" ".join(fruits))
print("_".join(fruits))
#12.  startswith()
text = "Python"
print(text.startswith("Py")) #Checks whether a string starts with a specific value.
#13.  endswith()
data = "data.csv"
print(data.endswith(".csv")) #Checks whether a string ends with a specific value.
# 14.  isalpha()
text = "Python"
print(text.isalpha()) #Checks whether the string contains only letters.
#15.  isdigit()
numbers = "12345"
print(numbers.isdigit()) #Checks whether the string contains only digits
#16.  isalnum()
text = "python123"
print(text.isalnum()) #Checks whether the string contains only letters and numbers.

#Mini practice 
name = "   nasir ali   "

print(name.strip())
print(name.upper())
print(name.title())
print(name.replace("ali", "asad"))
print(name.count("a"))
print(name.strip())

# 1. What is the difference between upper() and lower()?
# 2. What is the difference between split() and join()?
# 3. Why is strip() important in data cleaning?
# 4. What is the difference between find() and count()?
# 5. When would you use replace() in data analysis?

# Note:
# String methods are widely used in data cleaning and preprocessing.
# They help clean, format, and standardize text data before analysis.



