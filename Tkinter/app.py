import tkinter as tk
from tkinter import ttk
from mysql.connector import connect

db = {
    "host":"localhost",
    "user":"root",
    "password":"",
    "database":"pythondb"
}


root = tk.Tk()
root.title("Student Management")
def login(master):
        window = ttk.Frame(master, padding=(50, 40 , 50, 40))
        window.grid()
        master.geometry("320x180")
        ttk.Label(window, text="Username:").grid(column=0, row=0, sticky="E")
        ttk.Label(window, text="Password:").grid(column=0, row=1, sticky="E")

        username = tk.StringVar()
        password = tk.StringVar()
        ttk.Entry(window, textvariable=username).grid(column=1, row=0, sticky="W")
        ttk.Entry(window, textvariable=password, show="*").grid(column=1, row=1,pady=5, sticky="W")

        ttk.Button(window, text="Login", command=lambda: validation(master, window, username = username.get(), password=password.get())).grid(column=1, row=2, pady=5)

def validation(master, window, **kwargs):
    global heading
    if "user" in kwargs.values() and "admin" in kwargs.values():
        window.destroy()
        main_frame = ttk.Frame(master, padding = (5, 20, 5,))
        main_frame.grid()
        master.geometry("1215x400")

        button = ttk.Button(main_frame, text="Show students")
        button.grid(column=0, row=2, pady=5)
        button.configure(command=lambda: generateDataOfStudents(main_frame, button))
    else:
        ttk.Label(login_frame, text="Invalid username or password", foreground="red").grid(column=1, row=4, pady=5)

def generateDataOfStudents(window, button):
    button.grid_remove()
    treeview = ttk.Treeview(window, columns=("Student Id", "Idno", "Lastname", "Firstname", "Course", "Level"), show="headings")

    db_connection = connect(**db)
    cursor = db_connection.cursor()
    cursor.execute("select * from student")

    for i in range(len(treeview['columns'])):
        treeview.heading(treeview['columns'][i], text=treeview['columns'][i])
    for data in reversed(cursor.fetchall()):
       treeview.insert("", "0", values=(data[0],data[1],data[2],data[3],data[4],data[5]))
    treeview.grid(column=0, row=1)
    
    hide = ttk.Button(window, text="Hide")
    hide.grid(column=0, row=2, pady=50)
    hide.configure(command=lambda: clearTreeview(treeview, hide=hide, show=button))

    cursor.close()
    db_connection.close()

def clearTreeview(treeview, **button):
    treeview.grid_remove()
    button['show'].grid()
    button['hide'].grid_remove()

app = login(root)
root.mainloop()
