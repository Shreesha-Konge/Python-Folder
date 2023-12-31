#CLASS REPRESENT STUDENT
class Student:
    def __init__(self,name,age,grades):
        self.name=name
        self.age=age
        self.grades=grades
    def display_info(self):
        return f'Name:{self.name}\nAge:{self.age}\nGrades:{self.grades}'
S1=Student('Aradhya',25,'A')
S2=Student('Shree',24,'A')
print(S1.display_info())
print(S2.display_info())
        
