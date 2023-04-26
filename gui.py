import tkinter as tk
from tkinter import ttk
from employee import *

class startGui(tk.Tk):
    def __init__(self, manager):
        super().__init__()

        self.manager = manager
        self.title("Employee Management System")
        #self.geometry("400x300")
        self.table()        
        self.initializedEmployees()

        add_row_button = tk.Button(self, text="Add Row", command=lambda: insertRowDialog(self).show())
        add_row_button.grid(row = 0, column=0, columnspan=1)

    def table(self):
        self.table = ttk.Treeview(self, columns=("number", "name", "bDate", "age", "salary", "job_title"), show="headings")
        self.table.heading("#0", text="ID")
        self.table.heading("number", text="ID")
        self.table.heading("name", text="Name")
        self.table.heading("bDate", text="Birth Date")
        self.table.heading("age", text="Age")
        self.table.heading("salary", text="Salary")
        self.table.heading("job_title", text="Job Title")
        self.table.grid(row = 1, column=0, columnspan=10)
    
    def addRow(self, employee):
        id = employee.id
        self.table.insert(parent="", index="end", iid=id, text=id, values=(employee.id, employee.name, employee.bDate, employee.age, employee.salary, employee.job_title)) 

    def initializedEmployees(self):
        for employee in self.manager.employees:
            self.addRow(employee)


class insertRowDialog(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Add Row")
        
        self.name = tk.StringVar()        
        self.bDate = tk.StringVar()
        self.age = tk.StringVar()
        self.salary = tk.StringVar()
        self.job_title = tk.StringVar()
        
        name_label = tk.Label(self, text="Name:")
        name_label.grid(row=0, column=0)
        name_entry = tk.Entry(self, textvariable=self.name)
        name_entry.grid(row=0, column=1)

        bDate_label = tk.Label(self, text="Birth Date (m-d-Y):")
        bDate_label.grid(row=1, column=0)
        bDate_entry = tk.Entry(self, textvariable=self.bDate)
        bDate_entry.grid(row=1, column=1)
        
        #age_label = tk.Label(self, text="Age:")
        #age_label.grid(row=1, column=0)
        #age_entry = tk.Entry(self, textvariable=self.age)
        #age_entry.grid(row=1, column=1)
        
        salary_label = tk.Label(self, text="Salary:")
        salary_label.grid(row=2, column=0)
        salary_entry = tk.Entry(self, textvariable=self.salary)
        salary_entry.grid(row=2, column=1)
        
        job_title_label = tk.Label(self, text="Job Title:")
        job_title_label.grid(row=3, column=0)
        job_title_entry = tk.Entry(self, textvariable=self.job_title)
        job_title_entry.grid(row=3, column=1)
        
        add_button = tk.Button(self, text="Add", command=self.insertRow)
        add_button.grid(row=4, column=1)
        
    def insertRow(self):
        
        employee = self.master.manager.add_employee(self.name.get(), self.bDate.get(), self.salary.get(), self.job_title.get())
        self.master.addRow(employee)
        self.destroy()

    def show(self):
        self.wait_visibility()
        self.grab_set()
        self.wait_window()
