
#Topic: Dictionary Methods 
#Description: Learning the built-in methods of dictionary in Python 
#Author: Nasir Ali 

# What are Dictionary Methods?
# Dictionary Methods are built-in functions used to access, update, 
# remove and manage key-value pairs.

student = {
    "name": "Nasir",
    "age":25,
    "city":"Multan"
}
#1. keys()
print(student.keys())
#2. values()
print(student.values())
#3. items()
print(student.items())
#4. get()
print(student.get("name"))
print(student.get("salary"))
#5. update()
student.update({"salary":40000})
print(student)
student.update({
    "country":"Pakistan",
    "height":5.9
}) # multiple items 
print(student)
#6. pop()
student.pop("city")
print(student)
#7. popitem()
student.popitem()  # Removes the last inserted key-value pair
print(student)
#8. clear()
student.clear() # Remove all items 
print(student)

#9. copy()
person = {
    "name":"Ali",
    "age":20
}
new_person = person.copy()
print(new_person)

#10. setdefault()
student = {"name":"Nasir","age":25}
student.setdefault("city","Multan")
print(student)
student.setdefault("age",20)
print(student)

# Mini Practice 
employee = {
    "name":"Nasir",
    "salary":50000
}

print(employee.keys())
print(employee.values())
print(employee.items())
print(employee.get("salary"))
employee.update({"city":"Multan"})
print(employee)
employee.pop("salary")
print(employee)
new_employee = employee.copy()
print(new_employee)

#What I learned 

# keys()
# values()
# items()
# get()
# update()
# pop()
# popitem()
# clear()
# copy()
# setdefault()

# Interview Questions 

# 1. What is the difference between keys() and values()?
# 2. What does items() return?
# 3. What is the difference between get() and []?
# 4. What is the purpose of update()?
# 5. What does popitem() do?

# Note:
# Dictionary methods are widely used in
# APIs, JSON files, Pandas,
# and data analysis.
