import os,sys
import pwinput
from tabulate import tabulate

students:dict={"data":[]}

def addStudent():
    os.system("clear" if os.name == "posix" else "cls")
    student:dict={}
    print("Add Student \n----------------")
    student["idno"] =input("Idno        : ")
    student["firstname"] =input("Firstname   : ")
    student["lastname"] =input("Lastname    : ")
    student["course"] =input("Course      : ")
    student["level"] =input("Level       : ")
    students["data"].append(student)

    input("\nStudent added Succesfully Press any key to continue...")

def findStudent():
    os.system("clear" if os.name == "posix" else "cls")
    print("Find Student\n--------------")
    col = ["Idno","Firstname", "Lastname", "Course", "Level"]
    colmax = max(len(c) for c in col)
    l:list=[]
    isFound:bool=False

    find = input("Enter Idno of student: ")
    for i in students["data"]:
        if find == i.get("idno"):
            for k in i.values():
                l.append(k)
            isFound=True
    if isFound:
        print("")
        lmax = max(len(lm) for lm in l)
        for i in range(1,len(l)):
            
            print("{:<{}}".format(col[i], colmax+2) + ": " + "{:<{}}".format(l[i], lmax+2))

    else:print("\n\tStudent not existed")
    input("\n-----------------------------------------\nPress any key to continue..")
    
def deleteStudent():
    os.system("clear" if os.name == "posix" else "cls")
    print("Delete Student\n-------------------")
    todelete = input("Enter Idno: ")
    col = ["Idno", "Firstname", "Lastname", "Course", "Level"]
    colmax = max(len(c) for c in col)
    l:list=[]
    isDel:bool = False
    for i in students["data"]:
        if todelete == i.get("idno"):
            for j in i.values():
                l.append(j)
            isDel=True
    if isDel:
        lmax = max(len(lm) for lm in l)
        for i in range(len(l)):
            print("{:<{}}".format(col[i], colmax+2) + ": " + "{:<{}}".format(l[i],lmax+2))
        agreed:str = input("\n-----------------------------------------------------\nDo you really want to remove this student (y/n)?: ")

        if agreed == 'y':
            for i in range(len(students["data"])):
                if students["data"][i]["idno"] == todelete:
                    del students["data"][i]
                    input("Student removed. Press enter to continue..")

        else: isDel = False

def displayAll():
    os.system("clear" if os.name == "posix" else "cls")
    print("Display All Student\n-------------------")
    l = []
    col = ["Idno", "Firstname", "Lastname", "Course", "Level"]
    for i in students["data"]:
        p = []
        for k in i.values():
            p.append(k)
        l.append(p)
    if l != []:
        print(tabulate(l, headers=col))
    else:print("No records!")
    input("\n---------------------------------------------------\nPress any key to continue....")

def terminate():
    # os.system("clear")
    os.system("clear" if os.name == "posix" else "cls")
    print("Program Terminated")

def getMenuOption(option:int):
    options:dict={
        1:addStudent,
        2:findStudent,
        3:deleteStudent,
        4:displayAll,
        0:terminate
    }
    return options.get(option)()

def studentMenu():
    menu:tuple = (
        "-----Main Menu--------",
        "1: Add Student",
        "2: Find Student",
        "3: Update Student",
        "4: View all Student",
        "0: Terminate Program",
        "----------------------"
    )
    # os.system("clear")
    os.system("clear" if os.name == "posix" else "cls")
    print(*[menuValues for menuValues in menu],sep='\n')
    
def authenticate()->bool:
    # os.system("clear")
    os.system("clear" if os.name == "posix" else "cls")
    print("Login \n-----------------")
    user:str = input("Username: ")
    password:str = pwinput.pwinput(prompt="Password: ", mask="*")
    if user == "user" and password == "admin":
        return True
    return False

def main():
    isOkay:bool = authenticate()
    option:int = 999
    if isOkay:
        while option != 0:
            studentMenu()
            try:
                option = int(input("Enter option(1..4): "))
                getMenuOption(option)
            except:
                input("Invalid Input. Press any key to continue..")

    else:
        relog:int = int(input("\nInvalid Username or Password. \nLog in again? enter 1 for (Yes) and 0 for (No).: "))
        if relog == 1:
            main()
        else: os.system("clear" if os.name == "posix" else "cls"), print("Program Terminated"), sys.exit()
if __name__=="__main__":
    main()