import sqlite3

class DB:
    def __init__(self):
        self.conn = sqlite3.connect("db.sql")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                               (id INTEGER PRIMARY KEY,
                               name TEXT,
                               birthdate DATE,
                               age INTEGER,
                               salary REAL,
                               job_title TEXT)''')
        self.conn.commit()

    def get_all_employees(self):
        self.cursor.execute('SELECT * FROM employees ORDER BY id')
        rows = self.cursor.fetchall()
        return rows
    
    def insert(self, employee):
        self.cursor.execute('''INSERT INTO employees
                               (id, name, birthdate, age, salary, job_title)
                               VALUES (?, ?, ?, ?, ?, ?)''',
                            (employee.id, employee.name, employee.bDate,
                             employee.age, employee.salary, employee.job_title))
        self.conn.commit()

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

    def delete(self, employee_id):
        self.cursor.execute('DELETE FROM employees WHERE id = ?', (employee_id,))
        self.conn.commit()
