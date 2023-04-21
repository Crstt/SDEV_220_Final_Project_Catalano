from tkinter import *
from employee import *
from gui import *

gui = startGui()

# create an employee manager and add the employees
manager = EmployeeList()
manager.add_employee(Employee("John", 30, 50000, "Software Developer"))
manager.add_employee(Employee("Mary", 25, 45000, "Graphic Designer"))
manager.add_employee(Employee("Bob", 40, 60000, "Project Manager"))

# list the employees
manager.list_employees()

#start = Button(gui, text="START", text="Add", command=gui.addRowDialog)
#start.grid(row = 0, column=0, columnspan=1)

add_row_button = tk.Button(gui, text="Add Row", command=lambda: insertRowDialog(gui).show())
add_row_button.grid(row = 0, column=0, columnspan=1)

gui.mainloop()