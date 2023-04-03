import tkinter as tk
from tkinter import ttk
from mysql.connector import connect

db = {
    "host":"localhost",
    "user":"root",
    "password":"",
    "database":"pythondb"
}

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Management")
        self.main_frame = None
        self.login_frame = None
        self.login()

    def login(self):
        self.login_frame = ttk.Frame(self.master, padding=(50, 40 , 50, 40))
        self.login_frame.grid()
        self.master.geometry("320x180")
        ttk.Label(self.login_frame, text="Username:").grid(column=0, row=0, sticky="E")
        ttk.Label(self.login_frame, text="Password:").grid(column=0, row=1, sticky="E")

        self.username = tk.StringVar()
        self.password = tk.StringVar()
        ttk.Entry(self.login_frame, textvariable=self.username).grid(column=1, row=0, sticky="W")
        ttk.Entry(self.login_frame, textvariable=self.password, show="*").grid(column=1, row=1,pady=5, sticky="W")

        ttk.Button(self.login_frame, text="Login", command=self.management).grid(column=1, row=2, pady=5)

    def buttons(self):
        self.main_frame = ttk.Frame(self.master, padding = (5, 20, 5,))
        self.main_frame.grid()
        self.show = ttk.Button(self.main_frame, text="Show all students", width=20)
        self.show.grid(column=0, row=0, sticky="w")
        self.show.configure(command=self.generateDataOfStudents)

        self.add = ttk.Button(self.main_frame, text="Add student", width=20)
        self.add.grid(column=0, row=1,pady=5, sticky="w")
        self.add.configure(command=self.generateDataOfStudents)

        self.add = ttk.Button(self.main_frame, text="Add student", width=20)
        self.add.grid(column=0, row=2, sticky="w")
        self.add.configure(command=self.generateDataOfStudents)


    def management(self):
        if self.username.get() == "user" and self.password.get() == "admin":
            self.login_frame.destroy()

            self.buttons()

        else:
            ttk.Label(self.login_frame, text="Invalid username or password", foreground="red").grid(column=1, row=3)
    
    def generateDataOfStudents(self):
        self.show.grid_remove()
        self.add.grid_remove()
        self.master.geometry("1215x400")
        self.treeview = ttk.Treeview(self.main_frame, )
        self.treeview['columns'] = ("Student Id", "Idno", "Lastname", "Firstname", "Course", "Level")
        self.treeview['show'] = 'headings' 

        db_connectioin = connect(**db)
        cursor = db_connectioin.cursor()
        cursor.execute("select * from student")

        #set headings
        for i in range(len(self.treeview['columns'])):
            self.treeview.heading(self.treeview['columns'][i], text=self.treeview['columns'][i])
        #inserting data to treeview
        for data in reversed(cursor.fetchall()):
            self.treeview.insert("", "0", values=(data[0],data[1],data[2],data[3],data[4],data[5]))
        self.treeview.grid(column=0, row=1)

        self.hide = ttk.Button(self.main_frame, text="Hide")
        self.hide.grid(column=0, row=2, pady=50)
        self.hide.configure(command=self.clearTreeview)
    
    def clearTreeview(self):
        self.treeview.grid_remove()
        self.show.grid()
        self.add.grid()
        self.hide.grid_remove()
        self.master.geometry("320x180")

root = tk.Tk()
app = App(root)
root.mainloop()
