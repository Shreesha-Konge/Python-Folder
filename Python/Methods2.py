class Rectangle():
    def __init__(self,length=5,breadth=5):
        self.length = length
        self.breadth = breadth
    def getArea(self):
        return 2* (self.length + self.breadth)
r=Rectangle()
print(r.getArea())