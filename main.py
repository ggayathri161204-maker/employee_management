from tkinter import *
from tkinter import ttk, messagebox
from database import *

# Window
root = Tk()
root.title("Employee Performance Management System")
root.geometry("950x600")
root.configure(bg="white")

# Title
title = Label(
    root,
    text="Employee Performance Management System",
    font=("Arial", 20, "bold"),
    bg="white",
    fg="darkblue"
)
title.pack(pady=10)

# ===== Form Frame =====
form_frame = Frame(root, bg="white")
form_frame.pack(pady=10)

# Labels and Entries
Label(form_frame, text="Employee Name", bg="white", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)

name_entry = Entry(form_frame, width=25)
name_entry.grid(row=0, column=1)

Label(form_frame, text="Department", bg="white", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)

dept_entry = Entry(form_frame, width=25)
dept_entry.grid(row=1, column=1)

Label(form_frame, text="Designation", bg="white", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10)

desig_entry = Entry(form_frame, width=25)
desig_entry.grid(row=2, column=1)

Label(form_frame, text="Goals", bg="white", font=("Arial", 12)).grid(row=0, column=2, padx=10, pady=10)

goals_entry = Entry(form_frame, width=25)
goals_entry.grid(row=0, column=3)

Label(form_frame, text="Completed Tasks", bg="white", font=("Arial", 12)).grid(row=1, column=2, padx=10, pady=10)

tasks_entry = Entry(form_frame, width=25)
tasks_entry.grid(row=1, column=3)


# ===== Functions =====

def clear_fields():
    name_entry.delete(0, END)
    dept_entry.delete(0, END)
    desig_entry.delete(0, END)
    goals_entry.delete(0, END)
    tasks_entry.delete(0, END)


def add_data():

    name = name_entry.get()
    dept = dept_entry.get()
    desig = desig_entry.get()
    goals = goals_entry.get()
    tasks = tasks_entry.get()

    if name == "" or dept == "" or desig == "" or goals == "" or tasks == "":
        messagebox.showerror("Error", "All Fields are Required")
        return

    try:
        goals = int(goals)
        tasks = int(tasks)
    except:
        messagebox.showerror("Error", "Goals and Tasks must be numbers")
        return

    add_employee(name, dept, desig, goals, tasks)

    messagebox.showinfo("Success", "Employee Added Successfully")

    clear_fields()
    show_data()


def show_data():

    tree.delete(*tree.get_children())

    rows = get_employees()

    for row in rows:
        tree.insert("", END, values=row)


def delete_data():

    selected = tree.focus()

    if not selected:
        messagebox.showerror("Error", "Select Employee")
        return

    data = tree.item(selected)
    emp_id = data["values"][0]

    delete_employee(emp_id)

    messagebox.showinfo("Deleted", "Employee Deleted")

    show_data()


# ===== Buttons =====

btn_frame = Frame(root, bg="white")
btn_frame.pack(pady=10)

Button(
    btn_frame,
    text="Add Employee",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    width=15,
    command=add_data
).grid(row=0, column=0, padx=10)

Button(
    btn_frame,
    text="Delete Employee",
    font=("Arial", 12, "bold"),
    bg="red",
    fg="white",
    width=15,
    command=delete_data
).grid(row=0, column=1, padx=10)

Button(
    btn_frame,
    text="Refresh Data",
    font=("Arial", 12, "bold"),
    bg="blue",
    fg="white",
    width=15,
    command=show_data
).grid(row=0, column=2, padx=10)

# ===== Table =====

table_frame = Frame(root)
table_frame.pack(pady=20)

columns = (
    "ID",
    "Name",
    "Department",
    "Designation",
    "Goals",
    "Completed Tasks",
    "Performance Score"
)

tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=130)

tree.pack()

show_data()

root.mainloop()