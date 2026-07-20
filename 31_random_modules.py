
#Topic: Random Modules
#Description: Learning how to generate random values using Python's modules.
#Author: Nasir Ali 

#What is the Random Module?
#The random module is a built-in Python module used to generate the random numbers and make random selections.

#Why do we use the Random Modules?
#The random module is used to generate random numbers, select random items, shuffle data, and simuate randomness.

import random 


#1. randint()
# Return a random integer between two numbers
print(random.randint(1,8)) 
#2. randrange()
print(random.randrange(1,20))
print(random.randrange(1,15,2))
#3. choice()
fruits = ["apple","banana","mango", "grapes" ]
print(random.choice(fruits))
#4. choices()
fruits = ["apple","banana","mango", "grapes" ]
print(random.choices(fruits,k=2))
#5. shuffle 
numbers = [1,2,3,4,5,6]
random.shuffle(numbers)
print(numbers)
#6. random()
print(random.random())# 0 to 1 decimal num
#7. uniform()

#Mini Practice 

print(random.randint(50,100))
print(random.randrange(10,100,5))
colors = ["Red","Blue","Green","White"]
print(random.choice(colors))
numbers = [1,2,3,4,5]
random.shuffle(numbers)
print(numbers)
print(random.random())
print(random.uniform(100,200))

# What I learned
 
# random module
# randint()
# randrange()
# random()
# uniform()
# choice()
# choices()
# shuffle()

#Interview Questions

#What is the random module?
#What is the difference between randint() and randrange()?
#What does choice() do?
#What does shuffle() do?
#Which function returns a decimal number?


#Note:
#The random module is widely used in games,
#simulations, testing, password generation,
#and data analysis.

#اردو:

#Random Module کا استعمال Games،
#Testing، Simulations،
#Password Generation،
#اور Data Analysis میں کیا جاتا ہے۔
