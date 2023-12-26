import db as db
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

def welcome():
    print("Welcome, user! What service would you like to try?")
    print("\n1-Inserting data")
    print("\n2-Selecting data")
    print("\n3-Removing data")
    print("\n4-Updating data")
    print("\n5-Show statistics")
    print("\n6-Show graphs")
    print("\n7-Clear table")
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
            print(f"Student: {result[0][0]}\n")
            print(f"Hours of study: {result[0][1]}\n")
            print(f"Grades: {result[0][2]}\n")
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
        case 5:
            result = db.select_stats()
            hours,grades = zip(*result)
            # hours = list(map(lambda x: x[0], result))
            # grades = list(map(lambda x: x[1], result))
            print(f"Std.hours={np.std(hours)}\n")
            print(f"Std.grades={np.std(grades)}\n")
            pearsonr = sp.stats.pearsonr(hours,grades)
            print(f"Pearsonr.stats:\n")
            print(f"Correlation={pearsonr[0]},p-value={pearsonr[1]}")
        
        case 6:
            result = db.select_all()
            students,hours,grades = zip(*result)
            # students = list(map(lambda x: x[0], result))
            # hours = list(map(lambda x: x[1], result))
            # grades = list(map(lambda x: x[2], result))
            plt.scatter(hours,grades)
            for stud,hour,grade in zip(students,hours,grades):
                plt.annotate(stud,xy=(hour,grade),xytext=(5,-5),textcoords='offset points')
            plt.title("Hours x Grades")
            plt.xlabel("Hours")
            plt.ylabel("Grades")
            plt.show()
            
        case 7:
            result = db.clear()
            print("Operation done successfully")
            
        case _:
            print("Invalid Choice, try again")