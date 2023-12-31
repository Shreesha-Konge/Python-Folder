#CIRCLE AND SQUARE AREA AND PERIMETER
import math
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius**2
    def perimeter(self):
        return 2*math.pi*self.radius
class Square(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return self.length**2
    def perimeter(self):
        return 4*self.length
circle=Circle(20)
square=Square(20)
print(f'Circle area {circle.area()} & Perimeter {circle.perimeter()}')
print(f'Square area {square.area()} & Perimeter {square.perimeter()}')
        


        