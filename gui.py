from datetime import datetime
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox


class startGui(tk.Tk):
    def __init__(self, manager):
        super().__init__()

        self.manager = manager
        self.title("Employee Management System")
        # self.geometry("400x300")
        self.createTable()

        for employee in self.manager.employees:
            self.addRow(employee)

        add_row_button = tk.Button(
            self, text="Add Employee", command=lambda: changeEmployeeTable(self).show())
        add_row_button.grid(row=1, column=0, columnspan=1)
        add_row_button = tk.Button(
            self, text="Edit Employee", command=lambda: self.editRow())
        add_row_button.grid(row=1, column=1, columnspan=1)
        add_row_button = tk.Button(
            self, text="Remove Employee", command=lambda: self.removeRow())
        add_row_button.grid(row=1, column=2, columnspan=1)

        self.withdraw()
        description_window = EmployeeManagementSystemDescription(self)
        description_window.mainloop()
        EmployeeManagementSystemDescription()

    def createTable(self):
        self.table = ttk.Treeview(self, columns=(
            "number", "name", "bDate", "age", "salary", "job_title"), show="headings")
        self.table.heading("#0", text="ID")
        self.table.heading("number", text="ID")
        self.table.heading("name", text="Name")
        self.table.heading("bDate", text="Birth Date")
        self.table.heading("age", text="Age")
        self.table.heading("salary", text="Salary")
        self.table.heading("job_title", text="Job Title")
        self.table.grid(row=3, column=0, columnspan=3)

        # bind double-click to editRow function
        self.table.bind("<Double-Button-1>", self.editRow)

    def addRow(self, employee):
        id = employee.id
        self.table.insert(parent="", index="end", iid=id, text=id, values=(
            employee.id, employee.name, employee.bDate, employee.age, employee.salary, employee.job_title))

    def editRow(self, event=None):
        # Get the selected employee
        selected = self.table.selection()
        if selected:
            tableItem = self.table.item(selected[0])
            employee_id = tableItem["values"][0]
            employee = self.manager.getEmployeeByID(employee_id)
            changeEmployeeTable(self, "edit", employee).show()
            self.table.item(employee_id, text=employee_id, values=(
                employee.id, employee.name, employee.bDate, employee.age, employee.salary, employee.job_title))
        else:
            # Show an error message
            messagebox.showerror(
                "Error", "Please select an employee from the table.")

    def removeRow(self):
        # Get the selected employee
        selected = self.table.selection()
        if selected:
            tableItem = self.table.item(selected[0])
            employee_id = tableItem["values"][0]
            employee = self.manager.getEmployeeByID(employee_id)
            self.manager.remove_employee(employee)
            self.table.delete(employee_id)
        else:
            # Show an error message
            messagebox.showerror(
                "Error", "Please select an employee from the table.")


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

        self.name_valid = False
        self.bDate_valid = False
        self.salary_valid = False
        self.job_title_valid = False

        # Define validation functions
        def validate_name(text):
            self.name_valid = bool(text)
            if not self.name_valid:
                name_label.config(fg='red')
            else:
                name_label.config(fg='black')
            form_valid(self)
            return self.name_valid

        def validate_bDate(text):
            try:
                datetime.strptime(text, '%Y-%m-%d')
                self.bDate_valid = True
                bDate_label.config(fg='black')
            except ValueError:
                self.bDate_valid = False
                bDate_label.config(fg='red')
            form_valid(self)
            return self.bDate_valid

        def validate_salary(text):
            try:
                self.salary_valid = float(text) >= 0
                self.salary_valid = True
                salary_label.config(fg='black')
            except ValueError:
                self.salary_valid = False
                salary_label.config(fg='red')

            form_valid(self)
            return self.salary_valid

        def description_validate(text):
            self.job_title_valid = bool(text)
            if not self.job_title_valid:
                job_title_label.config(fg='red')
            else:
                job_title_label.config(fg='black')
            form_valid(self)
            return self.job_title_valid

        def form_valid(self):
            is_valid = self.name_valid and self.bDate_valid and self.salary_valid and self.job_title_valid
            # Enable the "Submit" button if the form is valid
            save_button.config(state="normal" if is_valid else "disabled")

        save_button_text = "Update" if self.mode == "edit" else "Add"
        save_button = tk.Button(
            self, text=save_button_text, command=self.saveRow)
        save_button.config(state="disabled")
        save_button.grid(row=4, column=1)

        # Set validation options for the entry fields
        name_validate_cmd = (self.register(validate_name), '%P')
        bDate_validate_cmd = (self.register(validate_bDate), '%P')
        salary_validate_cmd = (self.register(validate_salary), '%P')
        description_validate_cmd = (self.register(description_validate), '%P')

        name_label = tk.Label(self, text="Name:")
        name_label.grid(row=0, column=0)
        name_entry = tk.Entry(self, textvariable=self.name,
                              validate="focus", validatecommand=name_validate_cmd)
        name_entry.grid(row=0, column=1)

        bDate_label = tk.Label(self, text="Birth Date (Y-m-d):")
        bDate_label.grid(row=1, column=0)
        bDate_entry = tk.Entry(self, textvariable=self.bDate,
                               validate="focus", validatecommand=bDate_validate_cmd)
        bDate_entry.grid(row=1, column=1)

        salary_label = tk.Label(self, text="Salary:")
        salary_label.grid(row=2, column=0)
        salary_entry = tk.Entry(self, textvariable=self.salary,
                                validate="focus", validatecommand=salary_validate_cmd)
        salary_entry.grid(row=2, column=1)

        job_title_label = tk.Label(self, text="Job Title:")
        job_title_label.grid(row=3, column=0)
        job_title_entry = tk.Entry(self, textvariable=self.job_title,
                                   validate="focus", validatecommand=description_validate_cmd)
        job_title_entry.grid(row=3, column=1)

        if self.mode == "edit":
            self.name.set(self.employee.name)
            self.bDate.set(self.employee.bDate)
            self.salary.set(self.employee.salary)
            self.job_title.set(self.employee.job_title)

    def saveRow(self):
        if self.mode == "edit":
            self.employee.name = self.name.get()
            self.employee.bDate = self.bDate.get()
            self.employee.salary = self.salary.get()
            self.employee.job_title = self.job_title.get()
            self.master.manager.update_employee(self.employee)
        else:
            employee = self.master.manager.add_employee(
                self.name.get(), self.bDate.get(), self.salary.get(), self.job_title.get())
            self.master.addRow(employee)
        self.destroy()

    def show(self):
        self.wait_visibility()
        self.grab_set()
        self.wait_window()


class EmployeeManagementSystemDescription(tk.Toplevel):
    def __init__(self, root):
        super().__init__()
        self.title("Employee Management System Description")
        self.geometry("1000x300")
        self.root = root

        description_label = tk.Label(self, text="Welcome to the Employee Management System!\n\nThis program allows you to manage your company's employees. You can add, edit, and delete employee records using the user interface.\n\nTo get started, click the 'OK' button to view the list of current employees. From there, you can add new employees, edit existing employees, or delete employees as needed.\n\nThank you for using the Employee Management System!")
        description_label.pack(padx=20, pady=20)

        ok_button = tk.Button(self, text="OK", command=self.close_description)
        ok_button.pack(pady=10)

    def close_description(self):
        self.destroy()
        self.root.deiconify()
