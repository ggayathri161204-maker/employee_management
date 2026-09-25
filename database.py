import sqlite3

# Connect Database
conn = sqlite3.connect("employee.db")
cursor = conn.cursor()

# Employee Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department TEXT,
    designation TEXT,
    goals INTEGER,
    completed_tasks INTEGER,
    performance_score REAL
)
""")

conn.commit()


# Insert Employee
def add_employee(name, department, designation, goals, completed_tasks):
    
    performance_score = (completed_tasks / goals) * 100 if goals > 0 else 0

    cursor.execute("""
    INSERT INTO employees(name, department, designation, goals, completed_tasks, performance_score)
    VALUES(?,?,?,?,?,?)
    """, (name, department, designation, goals, completed_tasks, performance_score))

    conn.commit()


# Fetch Employees
def get_employees():
    cursor.execute("SELECT * FROM employees")
    return cursor.fetchall()


# Delete Employee
def delete_employee(emp_id):
    cursor.execute("DELETE FROM employees WHERE id=?", (emp_id,))
    conn.commit()