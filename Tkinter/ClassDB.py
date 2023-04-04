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
        self.add_frame = None
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
        
    def management(self):
        if self.username.get() == "a" and self.password.get() == "a":
            self.login_frame.destroy()
        
            self.master.geometry("310x130")
            self.buttonsForManagement()

        else:
            ttk.Label(self.login_frame, text="Invalid username or password", foreground="red").grid(column=1, row=3)

    def addStudnet(self):
        self.add_frame = ttk.Frame(self.master, padding=(50,40))
        self.add_frame.grid()
        self.main_frame.destroy()

        self.master.geometry("450x250")
        ttk.Label(self.add_frame, text="Enter idno:").grid(column=0, row=0, sticky="E")
        ttk.Label(self.add_frame, text="Firstname:").grid(column=0, row=1, sticky="E")
        ttk.Label(self.add_frame, text="Lastname:").grid(column=0, row=2, sticky="E")
        ttk.Label(self.add_frame, text="Course:").grid(column=0, row=3, sticky="E")
        ttk.Label(self.add_frame, text="Level:").grid(column=0, row=4, sticky="E")

        self.idno = tk.StringVar()
        self.lastname = tk.StringVar()
        self.firstname = tk.StringVar()
        self.course = tk.StringVar()
        self.level = tk.StringVar()
        ttk.Entry(self.add_frame, textvariable=self.idno).grid(column=1, row=0, sticky="w")
        ttk.Entry(self.add_frame, textvariable=self.lastname).grid(column=1, row=1, sticky="w")
        ttk.Entry(self.add_frame, textvariable=self.firstname).grid(column=1, row=2, sticky="w")
        ttk.Entry(self.add_frame, textvariable=self.course).grid(column=1, row=3, sticky="w")
        ttk.Entry(self.add_frame, textvariable=self.level).grid(column=1, row=4, sticky="w")

        # ttk.Entry(self.login_frame, textvariable=self.username).grid(column=1, row=0, sticky="W")
        # ttk.Entry(self.login_frame, textvariable=self.password, show="*").grid(column=1, row=1,pady=5, sticky="W")

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

        for i in range(len(self.treeview['columns'])):
            self.treeview.heading(self.treeview['columns'][i], text=self.treeview['columns'][i])#set headding

        for data in reversed(cursor.fetchall()):
            self.treeview.insert("", "0", values=(data[0],data[1],data[2],data[3],data[4],data[5]))#insert data
        self.treeview.grid(column=0, row=1)

        self.hide = self.dynamicButton(frame=self.main_frame, title="Hide", action=self.clearTreeview, width=20)
        self.hide.grid(column=0, row=4, pady=50)
    
    def clearTreeview(self):
        self.treeview.grid_remove()
        self.show.grid()
        self.add.grid()
        self.hide.grid_remove()
        self.master.geometry("310x130")

    def dynamicButton(self, **kwargs):
        button = ttk.Button(kwargs.get('frame'), text=f"{kwargs.get('title', '')}", command=kwargs.get('action'), width=kwargs.get('width'))
        return button

    def buttonsForManagement(self):
        self.main_frame = ttk.Frame(self.master, padding=(20, 40))
        self.main_frame.grid()

        self.show = self.dynamicButton(frame=self.main_frame, title="Show all students", action=self.generateDataOfStudents, width=20)
        self.show.grid(column=0, row=0, padx=(0,10))

        self.add = self.dynamicButton(frame=self.main_frame, title="Add student", action=self.addStudnet, width=20)
        self.add.grid(column=1, row=0,padx=(0,10))

        self.delete = self.dynamicButton(frame=self.main_frame, title="Delete student", width=20)
        self.delete.grid(column=0, row=1,padx=(0,10))

        self.update = self.dynamicButton(frame=self.main_frame, title="Update student", width=20)
        self.update.grid(column=1, row=1,padx=(0,10))

root = tk.Tk()
app = App(root)
root.mainloop()
