import tkinter as tk
from tkinter import ttk

class startGui(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Employee Management System")
        self.geometry("400x300")
        self.table()

    def table(self):
        self.table = ttk.Treeview(self, columns=("name", "age", "salary", "job_title"), show="headings")
        self.table.heading("#0", text="ID")
        self.table.heading("name", text="Name")
        self.table.heading("age", text="Age")
        self.table.heading("salary", text="Salary")
        self.table.heading("job_title", text="Job Title")
        self.table.grid(row = 1, column=0, columnspan=10)
    
    def addRow(self, data):
        id = len(self.table.get_children()) + 1
        self.table.insert(parent="", index="end", iid=id, text=id, values=data) 

class insertRowDialog(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Add Row")
        
        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.salary_var = tk.StringVar()
        self.job_title_var = tk.StringVar()
        
        name_label = tk.Label(self, text="Name:")
        name_label.grid(row=0, column=0)
        name_entry = tk.Entry(self, textvariable=self.name_var)
        name_entry.grid(row=0, column=1)
        
        age_label = tk.Label(self, text="Age:")
        age_label.grid(row=1, column=0)
        age_entry = tk.Entry(self, textvariable=self.age_var)
        age_entry.grid(row=1, column=1)
        
        salary_label = tk.Label(self, text="Salary:")
        salary_label.grid(row=2, column=0)
        salary_entry = tk.Entry(self, textvariable=self.salary_var)
        salary_entry.grid(row=2, column=1)
        
        job_title_label = tk.Label(self, text="Job Title:")
        job_title_label.grid(row=3, column=0)
        job_title_entry = tk.Entry(self, textvariable=self.job_title_var)
        job_title_entry.grid(row=3, column=1)
        
        add_button = tk.Button(self, text="Add", command=self.insertRow)
        add_button.grid(row=4, column=1)
        
    def insertRow(self):
        data = (self.name_var.get(), self.age_var.get(), self.salary_var.get(), self.job_title_var.get())
        self.master.addRow(data)
        self.destroy()

    def show(self):
        self.wait_visibility()
        self.grab_set()
        self.wait_window()
