import db as db

def welcome():
    print("Welcome, user! What service would you like to try?")
    print("\n1-Inserting data")
    print("\n2-Selecting data")
    print("\n3-Removing data")
    print("\n4-Updating data")
    return int(input())

def work(choice):
    match choice:
        case 1:
            print("Insert a student, the amount of hours it studiend and its grades: ")
            student, hours, grades = input().split()
            db.insert(student,int(hours),float(grades))
            print("Operation done successfully")
        case 2:
            print("Select a student: ")
            student = input()
            result = db.select(student)
            print("Showing results:\n")
            print(f"Estudante: {result[0][0]}\n")
            print(f"Horas estudadas: {result[0][1]}\n")
            print(f"Notas: {result[0][2]}\n")
            print("Operation done successfully")
        case 3:
            print("Select a student: ")
            student = input()
            result = db.remove(student)
            print("Operation done successfully")
        case 4:
            print("Insert a student, the amount of hours it studiend and its grades")
            student, hours, grades = input().split()
            db.update(student,int(hours),float(grades))
            print("Operation done successfully")
            
        case _:
            print("Invalid Choice, try again")