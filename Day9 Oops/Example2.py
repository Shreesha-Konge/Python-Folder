#EMPLOYEE DETAILS TO SHOW NAME,POSITON,SAL
class Employee:
    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=salary
    def display(self):
        return f'Name:{self.name}\nPosition:{self.position}\nSalary:{self.salary}'
employee_data=['Alice,Manager,70000','Aradhya,Professor,50000']
employees=[]
for data in employee_data:
    name,position,salary=data.split(',')
    salary=float(salary)
    employee=Employee(name,position,salary)
    employees.append(employee)
for employee in employees:
    print(employee.display())
    