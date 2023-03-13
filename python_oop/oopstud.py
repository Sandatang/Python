import os
from Oop import Student
from outhandler import outputHandler
import filehandler
import pwinput
from tabulate import tabulate

col:list=["Idno","Lastname","Firstname","Course","Level"]
student:list= []
isChanged = False
def addstudent():

    os.system("clear" if os.name=="posix" else "cls")
    print("Add Student")
    idno:str=input("Idno       :")
    lastname:str=input("Lastname   :")
    firstname:str=input("Firstname  :")
    course:str=input("Course     :")
    level:str=input("Level      :")
    student.append(Student(idno,lastname,firstname,course,level))

    input("Student added. Press enter key to continue...")

def findstudent():
    getData = filehandler.loadlist()
    os.system("clear" if os.name=="posix" else "cls")
    print("Find Student\n--------------------")
    idno=input("Idno: ")
    isfound=False

    if student:
        for i in student:
            if i.idno == idno:
                isfound=True
                os.system("clear" if os.name=="posix" else "cls")
                outputHandler("Found",i.idno,i.lastname,i.firstname,i.course,i.level)
                input("Press enter to continuee..")
    if getData:
        # data=[]
        for i in getData:
            for j in i:
                k = j.replace('[','').replace(']','').replace("'",'')
                if k == idno:
                    isfound=True
                    os.system("clear" if os.name=="posix" else "cls")
                    outputHandler("Found",k,i[1].strip().replace("'",''),i[2].strip().replace("'",''),i[3].strip().replace("'",''),i[4].strip().replace("]",'').replace("'",''))
                    input("Press enter to continuee..")
    if not(isfound):
        input("\nNo records!. \n\nPress enter to continue..")

def deletestudent():
    getData = filehandler.loadlist()
    os.system("clear" if os.name=="posix" else "cls")
    print("Delete Student\n-----------------------")
    idno=input("Idno: ")
    isfound=False
    
    if student:
        for i in student:
            if i.idno == idno:
                isfound=True
                os.system("clear" if os.name=="posix" else "cls")
                outputHandler("Deletion",i.idno,i.lastname,i.firstname,i.course,i.level)
                todel = input("Do you want to remove this student (y/n)?: ")
                if todel == 'y':
                    student.remove(i)
                    os.system("clear")
                    input("\nStudent deleted. Press enter to continue..")
                else:input("Operation cancelled!. Press enter to continue..")
    if getData:
        for i in getData:
            for j in i:
                k = j.replace('[','').replace(']','').replace("'",'')
                if k == idno:
                    isfound=True
                    os.system("clear" if os.name=="posix" else "cls")
                    outputHandler("Deletion",k,i[1].strip().replace("'",''),i[2].strip().replace("'",''),i[3].strip().replace("'",''),i[4].strip().replace("]",'').replace("'",''))

                    todel = input("Do you want to remove this student (y/n)?: ")
                    if todel == 'y':
                        filehandler.delete(idno)
                        isChanged=True
                        # importlib.reload(filehandler)
                        # getData = ''
                        input("\nStudent deleted. Press enter to continue..")
                    else:input("\nOperation cancelled!. Press enter to continue..")

    if not(isfound):
        input("\nNo records! \n\nPress enter to continue..")

def displaystudent():
    getData = filehandler.loadlist()
    os.system("clear" if os.name=="posix" else "cls")
    print("Display Students\n--------------------------------")
    data = []
    if getData:
        for i in getData:
            emptylist=[]
            for j in i:
                k = j.replace('[','').replace(']','').replace("'",'')
                emptylist.append(k)
            data.append(emptylist)
    if student:
        for i in student:
            data.append([i.idno,i.lastname,i.firstname,i.course,i.level])
    if data:
        print(tabulate(data, headers=col))
    else: print("No records!\n")
    input("Press enter to continue...")

def exit():

    os.system("clear" if os.name=="posix" else "cls")
    filehandler.saveit(student)
    print("Program Terminated")

def getOption(option:int)->str:

    options:dict={
        1:addstudent,
        2:findstudent,
        3:deletestudent,
        4:displaystudent,
        0:exit
    }
    return options.get(option)()

def menu():

    os.system("clear" if os.name == "posix" else "cls")
    menu:tuple=(
        "1. Add Student",
        "2. Find Student",
        "3. Delete Student",
        "4. Display All Student",
        "0. Quit/Exit",
        "-----------------------"
    )
    [print(i) for i in menu]

def login():

    okey:bool = False
    os.system("clear" if os.name == "posix" else "cls")
    print("Login")
    username:str = input("Username:")
    password:str = pwinput.pwinput(prompt="Password:",mask="*")

    if username == "user" and password == "admin":
        okey=True
    return okey

def main()->None:
    autheticated:bool = login()
    option:int = 999
    if autheticated:
        while option !=0:
            menu()
            # try:
            option:int=int(input("Enter option (0..4):"))
            getOption(option)
            # except:
            #     input("Invalid Input.")
    else: os.system("clear" if os.name=="posix" else "cls"),print("Invalid login. Please log in again")
if __name__ == "__main__":
    main()