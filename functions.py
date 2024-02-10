from datetime import date

PI = 3.14

def main():
    radius = float(input("Enter radius of a circle: "))
    print(f"Area of the circle with the radius {radius:.2f} is: {area_of_circle(radius):.2f}\n")

    num = int(input("Enter a number to calculate factorial of: "))
    if num < 0:
        print(f"Factorial of {num} cannot be calculated.\n")
    else:
        print(f"Factorial of {num} is: {factorial(num)}\n")
    
    birth_date = []
    print("You will be asked to enter your birth date separately as year, month, and day.")
    birth_date.append(int(input("Enter your birth year: ")))
    birth_date.append(int(input("Enter your birth month: ")))
    birth_date.append(int(input("Enter your birth day: ")))

    age = []
    age = calc_age(birth_date)
    print(f"You are {age[0]} years, {age[1]} months, {age[2]} days old.\n")

    is_retired(birth_date)

def area_of_circle(radius):
    return PI * (radius**2)

def factorial(num):
    fact = 1
    while num > 0:
        fact *= num
        num -= 1
    return fact

def calc_age(birth_date):
    today = date.today()
    birth_date = date(birth_date[0], birth_date[1], birth_date[2])

    age = today - birth_date
    years = age.days // 365
    months = (age.days % 365) // 30
    days = (age.days % 365) % 30

    return [years, months, days]

def is_retired(birth_date):
    age = calc_age(birth_date)
    
    if age[0] >= 65:
        print("You are retired.\n")
        return
    r_date = [64, 11, 30]
    r_date[0] = r_date[0] - age[0]
    r_date[1] = r_date[1] - age[1]
    r_date[2] = r_date[2] - age[2]
    
    print(f"You will retire in {r_date[0]} years, {r_date[1]} months, {r_date[2]} days.\n")

main()