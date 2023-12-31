#AREA AND PERIMETER OF RECTANGLE
class Rectangle:
    def __init__(self,length,width):
        self.len=length
        self.wid=width
    def area(self):
        self.area=self.len*self.wid
        return self.area
    def perimeter(self):
        self.perimeter=2*(self.len+self.wid)
        return self.perimeter
R=Rectangle(5,10)
print(R.area())
print(R.perimeter())

        
