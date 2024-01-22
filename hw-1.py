# Convert between the data types of the values assigned to the variables.
number = "12"
print(f"Type of the variable number is {type(number)}")

print(f"Type of the variable number after change is {type(int(number))}")

print(f"Type of the variable number after change is {type(float(int(number)))}\n")


""" The user is prompted to enter two values. The results of addition, 
subtraction, multiplication and division of the entered values are printed."""

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))

print(f"""\nAddition: {num1+num2}
Subtraction: {num1-num2}
Multiplication: {num1*num2}
Division: {num1/num2}""")


"""The user is asked for name, age, city and profession information and their answers are displayed."""
name = input("Enter your name: ")
age = int(input("Enter your age: "))
profession = input("Enter your profession: ")

print(f"\nName: {name}\nAge: {age}\nProfession: {profession}\n")

#The phrase "Hi-Kod Data Science Workshop" is initialized into a variable.
message = "Hi-Kod Data Science Workshop"

#Each word in the expression ("Hi-Kod", "Data", "Science", "Workshop") is selected from the variable.
list = message.split()
print(list) 

#The expression is converted to all uppercase letters. ("HI-KOD DATA SCIENCE WORKSHOP")
print(message.upper())

#Convert the expression to all uppercase letters. ("hi-kod data science workshop")
print(message.lower())

#Even numbers and odd numbers in the expression "0123456789" are selected. ("02468", "13579")

numbers = "0123456789"
myList = numbers.split()
