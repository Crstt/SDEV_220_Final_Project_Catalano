import tkinter as tk
from tkinter import ttk

class startGui(tk.Tk):
    def __init__(self, manager):
        super().__init__()

        self.manager = manager
        self.title("Employee Management System")
        #self.geometry("400x300")
        self.createTable()        

        for employee in self.manager.employees:
            self.addRow(employee)

        add_row_button = tk.Button(self, text="Add Employee", command=lambda: changeEmployeeTable(self).show())
        add_row_button.grid(row = 1, column=0, columnspan=1)
        add_row_button = tk.Button(self, text="Edit Employee", command=lambda: self.editRow())
        add_row_button.grid(row = 1, column=1, columnspan=1)
        add_row_button = tk.Button(self, text="Remove Employee", command=lambda: self.removeRow())
        add_row_button.grid(row = 1, column=2, columnspan=1)

    def createTable(self):
        self.table = ttk.Treeview(self, columns=("number", "name", "bDate", "age", "salary", "job_title"), show="headings")
        self.table.heading("#0", text="ID")
        self.table.heading("number", text="ID")
        self.table.heading("name", text="Name")
        self.table.heading("bDate", text="Birth Date")
        self.table.heading("age", text="Age")
        self.table.heading("salary", text="Salary")
        self.table.heading("job_title", text="Job Title")
        self.table.grid(row = 3, column=0, columnspan=3)
    
        self.table.bind("<Double-Button-1>", self.editRow)  # bind double-click to editRow function
    
    def addRow(self, employee):
        id = employee.id
        self.table.insert(parent="", index="end", iid=id, text=id, values=(employee.id, employee.name, employee.bDate, employee.age, employee.salary, employee.job_title)) 

    def editRow(self, event=None):
        # Get the selected employee
        selected = self.table.selection()
        if selected:
            tableItem = self.table.item(selected[0])
            employee_id = tableItem["values"][0]        
            employee = self.manager.getEmployeeByID(employee_id)
            changeEmployeeTable(self, "edit", employee).show()
            self.table.item(employee_id, text=employee_id, values=(employee.id, employee.name, employee.bDate, employee.age, employee.salary, employee.job_title))

    def removeRow(self):
         # Get the selected employee
        selected = self.table.selection()
        if selected:
            tableItem = self.table.item(selected[0])
            employee_id = tableItem["values"][0]        
            employee = self.manager.getEmployeeByID(employee_id)
            self.manager.remove_employee(employee)
            self.table.delete(employee_id)

class changeEmployeeTable(tk.Toplevel):
    def __init__(self, master, mode="insert", employee=None):
        super().__init__(master)
        self.title("Add Row")
        self.mode = mode
        self.employee = employee
        
        self.name = tk.StringVar()        
        self.bDate = tk.StringVar()
        self.salary = tk.StringVar()
        self.job_title = tk.StringVar()
        
        name_label = tk.Label(self, text="Name:")
        name_label.grid(row=0, column=0)
        name_entry = tk.Entry(self, textvariable=self.name)
        name_entry.grid(row=0, column=1)

        bDate_label = tk.Label(self, text="Birth Date (Y-d-m):")
        bDate_label.grid(row=1, column=0)
        bDate_entry = tk.Entry(self, textvariable=self.bDate)
        bDate_entry.grid(row=1, column=1)
        
        salary_label = tk.Label(self, text="Salary:")
        salary_label.grid(row=2, column=0)
        salary_entry = tk.Entry(self, textvariable=self.salary)
        salary_entry.grid(row=2, column=1)
        
        job_title_label = tk.Label(self, text="Job Title:")
        job_title_label.grid(row=3, column=0)
        job_title_entry = tk.Entry(self, textvariable=self.job_title)
        job_title_entry.grid(row=3, column=1)
        
        if self.mode == "edit":
            self.name.set(self.employee.name)
            self.bDate.set(self.employee.bDate)
            self.salary.set(self.employee.salary)
            self.job_title.set(self.employee.job_title)
        
        save_button_text = "Update" if self.mode == "edit" else "Add"
        save_button = tk.Button(self, text=save_button_text, command=self.saveRow)
        save_button.grid(row=4, column=1)

    def saveRow(self):
        if self.mode == "edit":
            self.employee.name = self.name.get()
            self.employee.bDate = self.bDate.get()
            self.employee.salary = self.salary.get()
            self.employee.job_title = self.job_title.get()
            self.master.manager.update_employee(self.employee)
        else:
            employee = self.master.manager.add_employee(self.name.get(), self.bDate.get(), self.salary.get(), self.job_title.get())
            self.master.addRow(employee)
        self.destroy()

    def show(self):
        self.wait_visibility()
        self.grab_set()
        self.wait_window()
