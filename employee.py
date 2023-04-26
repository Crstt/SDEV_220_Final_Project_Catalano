from datetime import datetime

class Employee:
    def __init__(self,id: int, name: str, bDate: str, salary: float, job_title: str):
        self.id = id
        self.name = name
        self.bDate = datetime.strptime(bDate, "%m-%d-%Y").date()
        self.age = int((datetime.now().date() - self.bDate).days / 365.25)
        self.salary = salary
        self.job_title = job_title
        
class EmployeeList:
    def __init__(self, db):
        self.employees = []
        
    def add_employee(self, name, bDate, salary, job_title):
        id = 0
        if self.employees:
            id = self.employees[-1].id + 1
        employee = Employee(id, name, bDate, salary, job_title)
        self.employees.append(employee)
        
        return employee
        
    def remove_employee(self, employee):
        self.employees.remove(employee)
        
    def list_employees(self):
        for employee in self.employees:
            print(f"{employee.id}, {employee.name}, {employee.bDate}, {employee.age}, {employee.salary}, {employee.job_title}")
