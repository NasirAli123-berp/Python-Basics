
#Topic: Date &Time Module 
#Description: Learning how to works with dates and time using the datetime module in Python.
#Author: Nasir Ali 

#What is the datetime Module?
#The datetime module is a built-in Python module used to work with dates and time.

import datetime 

#1. Current Date and Time 

print(datetime.datetime.now())

#2. Current Date Only

today = datetime.date.today()
print(today)

#3. Current Time Only 

now = datetime.datetime.now()
print(now.time())

#4. Year 

now = datetime.datetime.now()
print(now.year)

#5. Month 

now = datetime.datetime.now()
print(now.month)

#6. Day

now = datetime.datetime.now()
print(now.day)

#7. Hours
print(now.hour)
#8. Minute
print(now.minute)
#9. second 
print(now.second)

#10. Creating Your own Date
birthday= datetime.date(2001,4,5)
print(birthday)

#11. Creating Your Own Date and Time 
meeting = datetime.datetime(2026,7,20,2,10)
print(meeting)

#12. strftime()
now = datetime.datetime.now()
print(now.strftime("%d-%m-%y"))

# Formats
#%d = Day
#%m = Month
#%Y = Year
#%H = Hour (24)
#%M = Minute
#%S = Second

print(now.strftime("%d/%m/%Y"))

print(now.strftime("%H:%M:%S"))

# Mini Practice 
today = datetime.date.today()

birthday = datetime.date(2001,4,5)

difference = today - birthday

print(difference.days)
import datetime

today = datetime.date.today()

print(today)

now = datetime.datetime.now()

print(now.year)

print(now.month)

print(now.day)

print(now.strftime("%A"))

print(now.strftime("%B"))

print(now.strftime("%d/%m/%Y"))

#Note:
# The datetime module is widely used in
# automation, logging, web development,
# data analysis, and machine learning.

# اردو:
# datetime Module Automation، Logging،
# Data Analysis اور Real-world Applications میں
# بہت زیادہ استعمال ہوتا ہے۔