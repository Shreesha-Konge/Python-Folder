#AREA AND CIRCUMFERENCE OF CIRCLES
class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        self.area=self.pi*self.radius*self.radius
        return self.area
    def circumference(self):
        self.circumference=2*self.pi*self.radius
        return self.circumference
c=Circle(1)
print(c.area())
print(c.circumference())        