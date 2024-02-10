# function to display grade
def display_grade(students):
    name = input("Enter student name: ").capitalize()
    subject = input("Enter the subject name (Mathematics, Physics, Chemistry): ").capitalize()

    if name in students and subject in students[name]:
        print(f"Name: {name}\nSubject: {subject}\nGrade: {students[name][subject]}\n")
    else:
        print("Incorrect input.\n")

def add_student(students):
    name = input("Enter the name of the student to add to the dictionary: ").capitalize()
    math = int(input("Enter mathematics grade:"))
    phy = int(input("Enter physics grade:"))
    chem = int(input("Enter chemistry grade:"))

    if name not in students:
        students[name] = {"Mathematics": math, "Physics": phy, "Chemistry": chem}
    else:
        print("This student already exists.\n")

def change_grade(students):
    name = input("Enter the name of the student to change their grades: ").capitalize()
    subject = input("Enter the subject name you want to change (Mathematics, Physics, Chemistry): ").capitalize()
    grade = int(input("Enter the new grade: "))

    if name in students and subject in students[name]:
        students[name] = {subject: grade}
    else:
        print("Incorrect input.\n")

def display_info(students):
    name = input("Enter the name of the student to display their information: ").capitalize()
    if name not in students:
        print("Student does not exist")
        return
    print("Type 1 for Mathematics\nType 2 for Physics\nType 3 for Chemistry\nType 4 for all subjects\n")
    choice = int(input("--> "))

    match(choice):
        case 1:
            print(f"Mathematics: {students[name]['Mathematics']}\n")
        case 2:
            print(f"Physics: {students[name]['Physics']}\n")
        case 3:
            print(f"Chemistry: {students[name]['Chemistry']}\n")
        case 4:
            print(f"Mathematics: {students[name]['Mathematics']}\nPhysics: {students[name]['Physics']}\n")
            print(f"Chemistry: {students[name]['Chemistry']}\n")
        case _:
            print("Incorrect number\n")

def main():
    # dictionary to store students information
    students = {
        "John": {"Mathematics": 90, "Physics": 85, "Chemistry": 88},
        "Alice": {"Mathematics": 92, "Physics": 89, "Chemistry": 90},
        "Bob": {"Mathematics": 85, "Physics": 80, "Chemistry": 82},
        "Emily": {"Mathematics": 88, "Physics": 91, "Chemistry": 85},
        "Michael": {"Mathematics": 95, "Physics": 92, "Chemistry": 94},
        "Sophia": {"Mathematics": 89, "Physics": 86, "Chemistry": 90},
        "William": {"Mathematics": 91, "Physics": 87, "Chemistry": 93},
        "Emma": {"Mathematics": 86, "Physics": 84, "Chemistry": 88},
        "James": {"Mathematics": 90, "Physics": 88, "Chemistry": 89},
        "Olivia": {"Mathematics": 93, "Physics": 90, "Chemistry": 91}
    }
    #display_grade(students)
    add_student(students)
    print(students)
    change_grade(students)
    print(students)
    display_info(students)

main()