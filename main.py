from tkinter import *
from employee import *
from gui import *
from db import *

db = DB()

# create an employee manager and add the employees
manager = EmployeeList(db)
manager.add_employee("John", "02-05-1985", 50000, "Software Developer")
manager.add_employee("Mary", "7-23-1995", 45000, "Graphic Designer")
manager.add_employee("Bob", "10-15-1988", 60000, "Project Manager")

# list the employees
manager.list_employees()

gui = startGui(manager)
gui.mainloop()