
#Topic : File Handling 
#Description: Learning how to create, read, write and manage files in Python.
#Author: Nasir Ali 

#What is File Handling ?
#File Handling is the process of creating, reading, writing, updating, and deleting files using Python.

#Why do we use File Handling?
#We use File Handling to save data permanently instead of keeping it only in memory 

#File Modes

#"r" = read 
#"w" = write 
#"a" = append
#"x" = create

#1. Open a File 
file = open("00_python_syntax.py","r")
print(file)
file.close()

#2. Write Mode
file = open("data.txt","w")
file.write("Welcome to Python")
print(file)
file.close()

# multiple writing 
file = open("data.txt","w")
file.write("My name is Nasir Ali")
file.write("\nI am 25 year old")
file.write("\nI lived in Multan")
print(file)
file.close()

#3. Read File
file = open("00_python_syntax.py","r")
print(file.read())
file.close()

#4. Append Mode
file = open("data.txt","a")
file.write("\nLearning File Handling")
print(file)
file.close()

#5. Close File
file = open("data.txt","r")
print(file.read())
file.close()

#6. readline()
file = open("data.txt","r")
print(file.readline())
file.close()

#7. readlines()
file = open("data.txt","r")
print(file.readlines())
file.close

#8. with open()
with open("data.txt","r") as file:
	print(file.read())
# with open() automatically close the file 

#9. writing using with open()
with open("student.txt","w") as file:
	file.write("Welcome to Python by Nasir")

#10. appending using with open 	
with open("student.txt","a") as file:
	file.write("I am fine")

# Mini Practice 

with open("student.txt","w") as file:

    file.write("Name : Nasir\n")
    file.write("Age : 25\n")
    file.write("City : Multan")

with open("student.txt","r") as file:

    print(file.read())

with open("student.txt","a") as file:
	file.write("\nCountry : Pakistan")

with open("student.txt","r") as file:
	print(file.read())

#What I Learned 
	
# File Handling
# open()
# read()
# readline()
# readlines()
# write()
# append()
# close()
# with open()
# File Modes

#Interview Questions
#What is File Handling?
#What is the difference between read() and readline()?
#What is the difference between readline() and readlines()?
#What is the difference between "w" and "a" mode?
#Why is with open() better than open()?
#Does with open() require close()?
#What happens if you open a file in "w" mode?

#Note:
#English: with open() is the recommended and professional way to work with files because it automatically closes the file and makes the code cleaner.
#اردو: with open() فائل کے ساتھ کام کرنے کا Professional طریقہ ہے کیونکہ یہ فائل کو خودکار طور پر بند کر دیتا ہے اور کوڈ کو زیادہ صاف اور محفوظ بناتا ہے۔
