from employee import *
from gui import *
from db import *

db = DB()
# create an employee manager and add the employees
manager = EmployeeManager(db)
gui = startGui(manager)
gui.mainloop()