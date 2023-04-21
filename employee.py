class Employee:
    def __init__(self, name, age, salary, job_title):
        self.name = name
        self.age = age
        self.salary = salary
        self.job_title = job_title
        
class EmployeeList:
    def __init__(self):
        self.employees = []
        
    def add_employee(self, employee):
        self.employees.append(employee)
        
    def remove_employee(self, employee):
        self.employees.remove(employee)
        
    def list_employees(self):
        for employee in self.employees:
            print(f"{employee.name}, {employee.age}, {employee.salary}, {employee.job_title}")
