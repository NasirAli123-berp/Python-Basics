
#Topic: OS Module 
#Description: Learning how to interact with the operating systems using Python's os modules 
#Author: Nasir Ali 

#What is the OS Module?
#The os module is a built-in Python module used to interact the operating system, files and folders

#Why do we use the OS Module?

#Work with files and folders 
#Get the current working directory 
#Creat folders 
#Rename files or folders 
#Delete folders 
#Check whether a file and folder exists

#1. import os
import os

#2. Current working directory 
print(os.getcwd())  # Returns the current working directory.

#3. List Files and Folders 
print(os.listdir())

#4. Create a Folder 
import os 
os.mkdir("Python Notes")

#5. Rename Folder
os.rename("Python Notes","Python File")

#6. Remove Folder
os.rmdir("Python File")

#7. Check if File or Folder Exist 
print(os.path.exists("Python File"))

#8. Join Paths 
path = os.path.join("Python", "Notes", "Day1.py")

print(path)

#Mini Practice 

import os

print(os.getcwd())

print(os.listdir())

print(os.path.exists("Python"))

path = os.path.join("Data", "Files")
print(path)

#Interview Questions

#What is the os module?
#What does os.getcwd() do?
#What is the purpose of os.listdir()?
#How do you create a folder using Python?
#What does os.path.exists() return?


#Note
#English: The os module is widely used in automation, file handling, scripting, and data analysis projects.
#اردو: os Module Automation، File Handling، Scripts اور Data Analysis میں بہت زیادہ استعمال ہوتا ہے۔