# emplyee.py 
# Catalano Matteo
# 5/8/2023

from datetime import datetime

# Employee class describes the attributes of an employee
class Employee:
    def __init__(self,id: int, name: str, bDate: str, salary: float, job_title: str):
        self.id = id
        self.name = name
        self._bDate = datetime.strptime(bDate, "%Y-%m-%d").date()
        self.age = int((datetime.now().date() - self.bDate).days / 365.25)
        self.salary = salary
        self.job_title = job_title

    # these property are responsible for the update of the employee age when the birtdate is modified
    @property
    def bDate(self):
        return self._bDate

    @bDate.setter
    def bDate(self, value):
        self._bDate = datetime.strptime(value, "%Y-%m-%d").date()
        self.age = int((datetime.now().date() - self._bDate).days / 365.25)

# EmployeeManager class is responsible for managing all employees
# it contains a list of all employees in self.employees
class EmployeeManager:
    def __init__(self, db):
        self.db = db              
        self.employees = []

        rows = self.db.get_all_employees()  #get_all_employees is a function in the DB class that retrieves all employes saved in the database 
        #all rows from the query are added to the manager
        for row in rows:
            id, name, bDate, age, salary, job_title = row
            bDate = datetime.strptime(bDate, "%Y-%m-%d").strftime("%Y-%m-%d")
            employee = Employee(id, name, bDate, salary, job_title)
            self.employees.append(employee)

    #this function is reponsible to update the age when the birth date changes
    def bind_to_employee_updates(self, observer):
        self._observers.append(observer)

    # this function retrives an employee object from the list of employees from an id
    # Since all employees ids are in order from smallest to largest i was able to implement a binary search     
    def getEmployeeByID(self, id):
        left, right = 0, len(self.employees) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.employees[mid].id == id:
                return self.employees[mid]
            elif self.employees[mid].id < id:
                left = mid + 1
            else:
                right = mid - 1
        return None
    
    # add emplyess gets the detail of a new employees and adds it to the manager as well as saving it to the db
    def add_employee(self, name, bDate, salary, job_title):
        # if there are other employees the id is incremental 
        # if it is the first employee it is given the id 0
        id = 0        
        if self.employees:
            id = self.employees[-1].id + 1
        employee = Employee(id, name, bDate, salary, job_title)
        self.employees.append(employee) #employee is added to the list of employees
        self.db.insert(employee) #The insert function in the DB class is responsible for saving the new employee to the db 
        
        return employee
    
    # update_employee saves the modified employee object to the db
    def update_employee(self, employee):
        self.db.update(employee)        
        
    # remove_employee delets the employee object from the db
    def remove_employee(self, employee):
        self.db.delete(employee.id)
        self.employees.remove(employee)
        
    # list_employees is a deprecated function that lists all employees to the console
    def list_employees(self):
        for employee in self.employees:
            print(f"{employee.id}, {employee.name}, {employee.bDate}, {employee.age}, {employee.salary}, {employee.job_title}")
