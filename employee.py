from datetime import datetime

class Employee:
    def __init__(self,id: int, name: str, bDate: str, salary: float, job_title: str):
        self.id = id
        self.name = name
        self._bDate = datetime.strptime(bDate, "%Y-%m-%d").date()
        self.age = int((datetime.now().date() - self.bDate).days / 365.25)
        self.salary = salary
        self.job_title = job_title

    @property
    def bDate(self):
        return self._bDate

    @bDate.setter
    def bDate(self, value):
        self._bDate = datetime.strptime(value, "%Y-%m-%d").date()
        self.age = int((datetime.now().date() - self._bDate).days / 365.25)
        
class EmployeeManager:
    def __init__(self, db):
        self.db = db              
        self.employees = []

        rows = self.db.get_all_employees()  
        for row in rows:
            id, name, bDate, age, salary, job_title = row
            bDate = datetime.strptime(bDate, "%Y-%m-%d").strftime("%Y-%m-%d")
            employee = Employee(id, name, bDate, salary, job_title)
            self.employees.append(employee)

    def bind_to_employee_updates(self, observer):
        self._observers.append(observer)
        
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
    
    def add_employee(self, name, bDate, salary, job_title):
        id = 0
        if self.employees:
            id = self.employees[-1].id + 1
        employee = Employee(id, name, bDate, salary, job_title)
        self.employees.append(employee)
        self.db.insert(employee)
        
        return employee
    
    def update_employee(self, employee):
        self.db.update(employee)        
        
    def remove_employee(self, employee):
        self.db.delete(employee.id)
        self.employees.remove(employee)
        
    def list_employees(self):
        for employee in self.employees:
            print(f"{employee.id}, {employee.name}, {employee.bDate}, {employee.age}, {employee.salary}, {employee.job_title}")
