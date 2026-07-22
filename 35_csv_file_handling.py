
#Topic: CSV File Handling 
#Description: Learning how to read and write CSV(Comma-Separated Values) file in Python.
#Author: Nasir Ali 

#What is a CSV File ?
#A CSV(Comma-Separated Values) file store tabular data in rows and columns, where value are separated by commas.

#Why do we use CSV File?
#• Store tabular data
#• Exchange data between programs
#• Import data into Excel
#• Analyze data using Pandas 

#Import CSV Module 

import csv

#Writing CSV File 
with open("data.csv","w",newline="") as file:
	writer = csv.writer(file)
	writer.writerow(["Fruits","Kgs","Prices"])
	writer.writerow(["Apple",2,500])
	writer.writerow(["Mango",4,600])
     

# Reading CSV File 
with open("data.csv","r") as file:
	reader = csv.reader(file)
	for row in reader:
		print(row)
		
# Writing Multiple Rows

with open("student.csv","w",newline="") as file:
	writer = csv.writer(file)
	writer.writerow([
	["Name","Age","City"],
	["Nasir",25,"Multan"],
	["Ali",23,"Islamabad"],
	["Asad",27,"Karachi"]
])
	
#Append CSV File 
with open("student.csv","a",newline="") as file:
	writer = csv.writer(file)
	writer.writerow(["Amjad",33,"Peshawar "])

# Reading Each Columns

with open("student.csv","r") as file:
	reader = csv.reader(file)
	for row in reader:
		print("Name",row[0])
		print("age",row[1])
		print(row[2])

	
#Mini Practice 

import csv

with open("employees.csv","w",newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name","Salary","Department"])

    writer.writerows([
        ["Nasir",50000,"IT"],
        ["Ali",45000,"HR"],
        ["Sara",60000,"Finance"]
    ])

with open("employees.csv","r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)

	
# Interview Questions 

#What is a CSV file?
#Why do we use CSV files?
#What is the purpose of the csv module?
#What is the difference between writerow() and writerows()?
#Why do we use newline="" while writing CSV files?
#How do you read a CSV file in Python?
	
#Note:
#CSV files are the most common file format used in Data Analysis, Machine Learning, Excel, SQL, and Pandas.
