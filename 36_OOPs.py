
#Topic : Object- Oriented Programming (OOP Basics)
#Description: Leaning how to create objects and classes in Python.
#Author: Nasir Ali 

#What is OOP?
#English:
#Object-Oriented Programming (OOP) is a programming paradigm that organizes code using classes and objects.
# It helps create reusable, organized, and maintainable programs.
#اردو:
#Object-Oriented Programming (OOP) پروگرامنگ کا ایک طریقہ (Programming Paradigm) ہے جس میں پروگرام کو Classes اور Objects کی مدد سے منظم (Organize) کیا جاتا ہے۔ اس سے کوڈ دوبارہ استعمال (Reusable)، زیادہ صاف (Organized) اور آسانی سے Maintain ہونے والا بن جاتا ہے۔

#Why do we use OOP?

#Reuse code
#Organize large projects
#Reduce code repetition
#Make programs easier to maintain
#Represent real-world objects


#1. Creating First Class 
class Student:  #A class is created using the class keyword.
	pass
	
#2. Creating Object 
class Student:
	pass
student1 = Student()
print(student1)

#3. Class Attributes
class Student:
	name = "Nasir"  # Attribute
	age = 25   # Attribute
student1 = Student()
print(student1.name)
print(student1.age)

#4. Methods 

#What is self?
#self refers to the current object.
#It is used to access object attributes and methods.

class Student:
	def welcome(self):
		print("Welcome to Python")
student1 = Student()
student1.welcome()

#5. Constructor(__init__)
#What is __init__()?
#__init__() is a special method that automatically runs
#when an object is created.

class Student:
	def __init__(self):
		print("My Name is Nasir")
student = Student()
student = Student()

#6. Constructor with Parameters 
class Student:
	def __init__(self,name,age):
		self.name = name
		self.age = age
student1 = Student("Nasir",26)
print(student1.name)
print(student1.age)

#7. Multiple Objects

class Compressor:
	def __init__(self,company,kw, max_bar):
		self.company = company 
		self.kw = kw
		self.max_bar = max_bar
		
compressor1 = Compressor("Atlas Copco",560,7.7)
compressor2 = Compressor("Wuxi",37,7.0)
compressor3 = Compressor("Honda",630,8.5)
print(compressor1.company)
print(compressor2.kw)
print(compressor3.max_bar)

#8. Methods with Attributes 
class Student:
	def __init__(self,name):
		self.name = name 
	def welcome(self):
			print("Hello", self.name)
student1= Student("Nasir")
student2 = Student("Ali")
student1.welcome()
student2.welcome()


#Mini Practice 

factory = {
    "morning temp C⁰":[27,31,39],
    "evening temp C⁰": [25,30,28],
    "night temp C⁰":[26,34,30]
}

class Temp_Analyzer:
	def __init__(self):
		self.data = {}
		
	def add_shift(self, shift_name, temperature):
		self.data[shift_name] = temperature 
		
	def shift_average(self, shift_name):
		data = self.data[shift_name]
		average = sum(data)/len(data)
		
		print(f"{shift_name} average= {average:.2f}%")
analyzer = Temp_Analyzer()
for shift,temps in factory.items():
		analyzer.add_shift(shift, temps)
analyzer.shift_average("morning temp C⁰")
analyzer.shift_average("evening temp C⁰")
analyzer.shift_average("night temp C⁰")		
#Interview Questions

#What is Object-Oriented Programming (OOP)?
#Why do we use OOP?
#What is a Class?
#What is an Object?
#What is the difference between a Class and an Object?
#What is an Attribute?
#What is a Method?
#What is the purpose of self?
#What is the __init__() method?
#What is a Constructor?
#Can we create multiple objects from one class?
#What is the difference between a Function and a Method?

#Note
#English:
#OOP is one of the most powerful programming concepts. It is widely used in Software Development, Web Development, Automation, Game Development, Machine Learning, and Data Analysis. Learning OOP makes it easier to build large and organized applications.
#اردو:
#OOP پروگرامنگ کے سب سے اہم تصورات میں سے ایک ہے۔ یہ Software Development، Web Development، Automation، Game Development، Machine Learning اور Data Analysis میں وسیع پیمانے پر استعمال ہوتی ہے۔ OOP سیکھنے سے بڑے اور منظم پروگرام بنانا آسان ہو جاتا ہے۔		