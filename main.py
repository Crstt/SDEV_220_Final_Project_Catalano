# SDEV 220 - main.py - Final Project - Employee Management System
# Catalano Matteo
# 5/8/2023
# In this system, I will create an Employee class that will store information about each employee, such as their name, age, salary, and job title. 
# I will also create an EmployeeManager class that will manage all the employees and provide methods for adding, removing, and listing employees. 
# The scope of the Employee Management System is to provide a user-friendly interface for managing employee information, including adding new employees, removing existing employees, and listing all employees.

from employee import *
from gui import *
from db import *

# create a db instance
db = DB()
# create an employee manager instance
manager = EmployeeManager(db)
# create a gui instance
gui = StartGui(manager)
#starts the gui main loop
gui.mainloop()
