# db.py 
# Catalano Matteo
# 5/8/2023

import sqlite3

# The DB class is responsible for interacting with the database
class DB:
    # The init function creates a connection with the db.sql 
    # if the db is not found a new one is created with the appropriate structure
    def __init__(self):
        self.conn = sqlite3.connect("db.sql")
        self.cursor = self.conn.cursor()
        self.create_table()

    #this function creates the table that will store the employees
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                               (id INTEGER PRIMARY KEY,
                               name TEXT,
                               birthdate DATE,
                               age INTEGER,
                               salary REAL,
                               job_title TEXT)''')
        self.conn.commit()

    # this funciton retrieves all employees from the db in order of id
    def get_all_employees(self):
        self.cursor.execute('SELECT * FROM employees ORDER BY id')
        rows = self.cursor.fetchall()
        return rows
    
    # this function adds a new employee record based on the employee object that it recieved
    def insert(self, employee):
        self.cursor.execute('''INSERT INTO employees
                               (id, name, birthdate, age, salary, job_title)
                               VALUES (?, ?, ?, ?, ?, ?)''',
                            (employee.id, employee.name, employee.bDate,
                             employee.age, employee.salary, employee.job_title))
        self.conn.commit()

    # this function updates an employee record based on the employee object that it recieved
    def update(self, employee):
        self.cursor.execute('''UPDATE employees SET
                               name = ?,
                               birthdate = ?,
                               age = ?,
                               salary = ?,
                               job_title = ?
                               WHERE id = ?''',
                            (employee.name, employee.bDate, employee.age,
                             employee.salary, employee.job_title, employee.id))
        self.conn.commit()

    # this function deletes an employee record based on the employee id that it recieved
    def delete(self, employee_id):
        self.cursor.execute('DELETE FROM employees WHERE id = ?', (employee_id,))
        self.conn.commit()
