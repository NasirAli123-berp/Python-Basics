
#Topic: Dictionary 
#Description: Learning the fundamentals of dictionaries in Python 
#Author: Nasir Ali 

# What is a Dictionary?
# Dictionary is an unordered and mutable collection of key-value pairs.
# Example 
student = {
    "name": "Nasir",
    "age": 25,
    "city": "Multan"
}
#name -----> Key   #name is key

#Nasir -----> Value   # Nasir is value

# Creating Dictionary 
my_dict = {
    "name":"Ali",
    "age":25,
    "city":"Multan"
}
print(my_dict)
# Type Dictionary 
print(type(my_dict))

# Empty Dictionary 
null_dict = {}
print(type(null_dict))

# Different Data Types 
data= {
    "name":"Nasir",
    "age":25,
    "height":5.9,
    "student": True
}
print(data)
# len()
print(len(data))
# Membership 
print("age" in data)
print("salary" in data)
# Note:
# 'in' checks only keys, not values.
# Accessing Values 
print(data["name"])
print(data["student"])
# get()
print(data.get("age"))
print(data.get("salary")) # None

# Updating Values 
data["name"] = "Ali"
print(data)
# Adding New Items 
data["country"] = "Pakistan"
print(data)
# Removing Items 
data.pop("student")
print(data)

# Nested Dictionary 
subjects = {
    "book":"Computer",
    "marks":{
        "student1":89,
        "student2":93,
        "student3":96
    }
}
print(subjects)
print(subjects["marks"])
print(subjects["marks"]["student2"])

# Mini Practice 
company = {
    "name":"Fazal Cloth",
    "depart":"Compressor",
    "salary":40000,
    "city": "Multan"
}
print(company)
print(type(company))
print("depart" in company)
print(company["city"])
print(company.get("salary"))
company["depart"] = "Air Conditions "
print(company)
company["country"] = "Pakistan"
print(company)
print(len(company))
print(company.keys())
print(company.values())

# What I learned 

# Creating Dictionaries
# Key-Value Pairs
# Different Data Types
# type()
# Accessing Values
# get()
# Updating Values
# Adding New Items
# Removing Items
# Membership
# Nested Dictionaries
# len()

# Interview Questions 
# 1. What is a dictionary?
# 2. What is the difference between a list and a dictionary?
# 3. What is the difference between [] and get()?
# 4. What are keys and values?
# 5. Can a dictionary store different data types?

# Note:
# Dictionaries are one of the most important
# data structures in Python.
# They are widely used in APIs,
# JSON data, Pandas,
# and data analysis.


