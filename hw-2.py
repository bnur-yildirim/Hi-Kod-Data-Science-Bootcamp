#The user is asked for their salary information and based on this
#information, how much tax will be deducted from her salary is calculated.
salary = float(input("Enter your salary: "))

if salary <= 10000:
    salary -= salary * 0.05
elif salary <= 25000:
    salary -= salary * 0.10
elif salary <= 45000:
    salary -= salary * 0.25
else:
    salary -= salary * 0.30
print(f"New salary after tax payment is {salary}\n")

"""
The user is asked to create a username and password. 
If the length of the password reaches six digits,
you will receive the message that your account has been created; 
if it is less than six digits, you will receive the message that
a six-digit password must be created.
"""
username = input("Create a username: ")
password = input("Enter a password: ")

if len(password) >= 6:
    print("Account created.\n")
else:
    print("Length of your password must be greater than 6 digits.\n")

#The previous example is improved.
#The password entered by the user must be between 5 and 10 digits.
#If it meets this condition, "Your account has been created." is printed.
#else, "The password should be greater than 5 digits and less than 10 digits!" printed
#it continues to ask until the user creates a password in the conditions we want.
while len(password) < 5 or len(password) > 10:
    password = input("Length of the password should be between 5 and 10: ")
print("Account created.\n")

# User will be prompt to enter username and password, and three tries are given for password entry.
_username = input("Enter your username: ")
_password = input("Enter your password: ")
tries = 3

while tries > 0:
    if password == _password:
        print("Logged in.\n")
        break
    else:
        _password = input(f"Wrong password. You have {tries} tries.\nEnter again: ")
        tries -= 1



