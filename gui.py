# gui.py 
# Catalano Matteo
# 5/8/2023

from datetime import datetime
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox

# start gui class is the class that manages the entire gui
# self will rappresent the root page
# manager is the class where the employees are stored 
class StartGui(tk.Tk):
    def __init__(self, manager):
        super().__init__()

        # Colors used in the program
        self.bg = "#242734" #primary background color
        self.bgSecondary = "#333646" #secondary background color
        self.accentColor = "#54b3d6" #accent color

        self.manager = manager #manager is the class where the employees are stored
        self.title("Employee Management System")
        self.configure(bg=self.bg)
        self.createTable()

        #loads all emplyes from the database to the table
        for employee in self.manager.employees:
            self.addRow(employee)


        #sets and places header for root
        heading = tk.Label(self, text="Employee Management System", font=( "Arial", 16), fg="white", bg=self.bg)
        heading.grid(row=0, column=0, columnspan=3)

        #creates the buttons for root
        add_row_button = tk.Button(self, text="Add Employee", command=lambda: ChangeEmployeeTable(self).show())
        edit_button = tk.Button(self, text="Edit Employee", command=lambda: self.editRow())
        remove_button = tk.Button(self, text="Remove Employee", command=lambda: self.removeRow())

        #places the buttons on root
        add_row_button.grid(row=1, column=0, columnspan=1)
        edit_button.grid(row=1, column=1, columnspan=1)
        remove_button.grid(row=1, column=2, columnspan=1)

        #styles the buttons on root
        self.styleButtons(add_row_button, self.accentColor, self.bg)
        self.styleButtons(edit_button, self.accentColor, self.bg)
        self.styleButtons(remove_button, self.accentColor, self.bg)

        self.withdraw() #hides root

        #calls and runs the welcome page
        description_window = EmployeeManagementSystemDescription(self)
        description_window.mainloop()

    #this function initializes the table that will be displayed on the root page
    def createTable(self):
        self.table = ttk.Treeview(self, columns=(
            "number", "name", "bDate", "age", "salary", "job_title"), show="headings")
        
        # initializes the headers for the table
        self.table.heading("#0", text="ID")
        self.table.heading("number", text="ID")
        self.table.heading("name", text="Name")
        self.table.heading("bDate", text="Birth Date")
        self.table.heading("age", text="Age")
        self.table.heading("salary", text="Salary")
        self.table.heading("job_title", text="Job Title")

        # sets sze of the headers for the table and centers the text
        self.table.column("#0", anchor='center', width=50, stretch=False)
        self.table.column("number", anchor='center', width=100, stretch=False)
        self.table.column("name", anchor='center', width=150, stretch=False)
        self.table.column("bDate", anchor='center', width=100, stretch=False)
        self.table.column("age", anchor='center', width=50, stretch=False)
        self.table.column("salary", anchor='center', width=100, stretch=False)
        self.table.column("job_title", anchor='center', width=200, stretch=False) 

        #creates a style for the table
        self.style = ttk.Style()
        self.style.theme_use("clam")

        #style configuration for the body of the table
        self.style.configure("Treeview", 
                        background= self.bg,
                        foreground="white",
                        fieldbackground=self.bg,
                        bordercolor="white",
                        font=("Arial", 12))
        self.style.map("Treeview.Heading", background=[("active", self.bg)]) #removes style when mouse overs over the headers of the table

        #style for the headers
        self.style.configure("Treeview.Heading", 
                        background=self.bg,
                        foreground="white",
                        font=("Arial", 12, "bold"),
                        bordercolor="white")

        # bind double-click to editRow function
        self.table.bind("<Double-Button-1>", self.editRow)

        # inizializes scrollbar for the table
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.table.yview)
        scrollbar.grid(row=3, column=4, sticky="ns")

        # attach the scrollbar to the table
        self.table.configure(yscrollcommand=scrollbar.set)

        #places table on root
        self.table.grid(row=3, column=0, columnspan=3)

    #addRow is the function responsable to adding new emplyees to the table
    # self is the root window
    # employee is the object that rapresents the new employee
    def addRow(self, employee):
        id = employee.id
        self.table.insert(parent="", index="end", iid=id, text=id, values=(
            employee.id, employee.name, employee.bDate, employee.age, employee.salary, employee.job_title))

    # editRow is the funcion that is called when pressing edit employee or duble clicking on an employee in the table
    # self is the root window
    def editRow(self, event=None):
        # Get the selected employee
        selected = self.table.selection()
        if selected:
            tableItem = self.table.item(selected[0]) #gets selected employee
            employee_id = tableItem["values"][0]
            employee = self.manager.getEmployeeByID(employee_id) #this function is in the employeeManager class and is responsible for managing the editing of the employee
            ChangeEmployeeTable(self, "edit", employee).show() # this line calls the class that manages the pop up window for editing and adding employees
            self.table.item(employee_id, text=employee_id, values=(
                employee.id, employee.name, employee.bDate, employee.age, employee.salary, employee.job_title))
        else:
            # Show an error message when an employee is not selectd
            messagebox.showerror(
                "Error", "Please select an employee from the table.")

    # removeRow is the function responsible for removing an employee from the system
    # self is the root window
    def removeRow(self):
        # Get the selected employee
        selected = self.table.selection()
        if selected:
            tableItem = self.table.item(selected[0]) #gets selected employee
            employee_id = tableItem["values"][0]
            employee = self.manager.getEmployeeByID(employee_id)
            self.manager.remove_employee(employee) #this function is in the employeeManager class and is responsible for managing the removal of the employee
            self.table.delete(employee_id)
        else:
            # Show an error message when an employee is not selectd
            messagebox.showerror(
                "Error", "Please select an employee from the table.")

    # this function applys a style to the buttons
    def styleButtons(self, button, colorOnHover, colorOnLeave):

        button.config(width = 20, bg=colorOnLeave, fg="white", bd=0, font=("bold"), highlightthickness=1, highlightcolor="white", highlightbackground="white")

        # adjusting backgroung of the widget
        # background on entering widget
        button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))
        # background color on leving widget
        button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))

# this class manages the pop up windows that adds or edits employees
# self is the pop up window
# master is the root window
# mode is the mode of the window (insert / edit)
class ChangeEmployeeTable(tk.Toplevel):
    def __init__(self, master, mode="insert", employee=None):
        super().__init__(master)
        self.title("Add Row")
        self.mode = mode
        self.employee = employee        
        self.configure(bg= master.bg)

        self.name = tk.StringVar()
        self.bDate = tk.StringVar()
        self.salary = tk.StringVar()
        self.job_title = tk.StringVar()

        self.name_valid = False
        self.bDate_valid = False
        self.salary_valid = False
        self.job_title_valid = False

        # Define validation functions
        # name must not be empty
        def validate_name(text):
            self.name_valid = bool(text)
            if not self.name_valid:
                name_label.config(fg='red')
            else:
                name_label.config(fg='white')
            form_valid(self)
            return self.name_valid

        # date must be valid date in the format Y-m-d 
        def validate_bDate(text):
            try:
                datetime.strptime(text, '%Y-%m-%d')
                self.bDate_valid = True
                bDate_label.config(fg='white')
            except ValueError:
                self.bDate_valid = False
                bDate_label.config(fg='red')
            form_valid(self)
            return self.bDate_valid

        #salary must be a valid float
        def validate_salary(text):
            try:
                self.salary_valid = float(text) >= 0
                self.salary_valid = True
                salary_label.config(fg='white')
            except ValueError:
                self.salary_valid = False
                salary_label.config(fg='red')

            form_valid(self)
            return self.salary_valid

        # description must not be empty
        def description_validate(text):
            self.job_title_valid = bool(text)
            if not self.job_title_valid:
                job_title_label.config(fg='red')
            else:
                job_title_label.config(fg='white')
            form_valid(self)
            return self.job_title_valid

        # form valid makes sure that the form has all valid values and enables the submit button
        # or disables it if any of the values are not valid
        def form_valid(self):
            is_valid = self.name_valid and self.bDate_valid and self.salary_valid and self.job_title_valid
            # Enable the "Submit" button if the form is valid
            save_button.config(state="normal" if is_valid else "disabled")

        #save buttons depends on the mode of the pop up window insert/edit
        save_button_text = "Update" if self.mode == "edit" else "Add"
        save_button = tk.Button(self, text=save_button_text, command=self.saveRow)
        save_button.config(state="disabled") #state is defaulted as disabled
        master.styleButtons(save_button, master.accentColor, master.bg)
        #places the button on the popup window
        save_button.grid(row=4, column=1)

        label_submit = tk.Label(self, text="When form is complete\ndeselect current textbox")
        label_submit.config(font=( "Arial", 8), fg="#999AA2", bg=master.bg)
        label_submit.grid(row=4, column=0)

        # Set validation options for the entry fields
        name_validate_cmd = (self.register(validate_name), '%P')
        bDate_validate_cmd = (self.register(validate_bDate), '%P')
        salary_validate_cmd = (self.register(validate_salary), '%P')
        description_validate_cmd = (self.register(description_validate), '%P')

        name_label = tk.Label(self, text="Name:")
        name_label.config(font=( "Arial", 12), fg="white", bg=master.bg)
        name_label.grid(row=0, column=0)
        name_entry = tk.Entry(self, textvariable=self.name, validate="key", validatecommand=name_validate_cmd) 
        name_entry.grid(row=0, column=1)

        bDate_label = tk.Label(self, text="Birth Date (Y-m-d):")        
        bDate_label.config(font=( "Arial", 12), fg="white", bg=master.bg)
        bDate_label.grid(row=1, column=0)
        bDate_entry = tk.Entry(self, textvariable=self.bDate, validate="focusout", validatecommand=bDate_validate_cmd)
        bDate_entry.grid(row=1, column=1)

        salary_label = tk.Label(self, text="Salary:")
        salary_label.config(font=( "Arial", 12), fg="white", bg=master.bg)
        salary_label.grid(row=2, column=0)
        salary_entry = tk.Entry(self, textvariable=self.salary, validate="focusout", validatecommand=salary_validate_cmd)
        salary_entry.grid(row=2, column=1)

        job_title_label = tk.Label(self, text="Job Title:")
        job_title_label.config(font=( "Arial", 12), fg="white", bg=master.bg)
        job_title_label.grid(row=3, column=0)
        job_title_entry = tk.Entry(self, textvariable=self.job_title, validate="key", validatecommand=description_validate_cmd)
        job_title_entry.grid(row=3, column=1)

        # if the mode is edit the values of the current selected employee are populated in the field
        if self.mode == "edit":
            self.name.set(self.employee.name)
            self.bDate.set(self.employee.bDate)
            self.salary.set(self.employee.salary)
            self.job_title.set(self.employee.job_title)

    # saveRow gets the values from the form and seds the values to the appropriate function in the employeeManager class
    def saveRow(self):
        if self.mode == "edit":
            self.employee.name = self.name.get()
            self.employee.bDate = self.bDate.get()
            self.employee.salary = self.salary.get()
            self.employee.job_title = self.job_title.get()
            self.master.manager.update_employee(self.employee) #update_employee updates the value of an existing employee
        else:
            employee = self.master.manager.add_employee(self.name.get(), self.bDate.get(), self.salary.get(), self.job_title.get()) #add_employee adds a new employee
            self.master.addRow(employee) #employee is added to the table
        self.destroy() #popup window is closed

    def show(self):
        self.wait_visibility()
        self.grab_set()
        self.wait_window()

# this class is responsible for managing the welcome window at the start of the program
class EmployeeManagementSystemDescription(tk.Toplevel):
    def __init__(self, root):
        super().__init__()
        self.title("Employee Management System Description")
        self.root = root
        self.configure(bg=self.root.bg)

        description_label = tk.Label(self, text="Welcome to the Employee Management System!\n\nThis program allows you to manage your company's employees. You can add, edit, and delete employee records using the user interface.\n\nTo get started, click the 'OK' button to view the list of current employees. From there, you can add new employees, edit existing employees, or delete employees as needed.\n\nThank you for using the Employee Management System!")
        description_label.config(font=( "Arial", 16), fg="white", bg=self.root.bg)
        description_label.pack(padx=20, pady=20)

        ok_button = tk.Button(self, text="OK", command=self.close_description)
        self.root.styleButtons(ok_button, self.root.accentColor, self.root.bg)
        ok_button.pack(pady=10)

    def close_description(self):
        self.destroy()
        self.root.deiconify()
