class Circle():
    #CLASS OBJECT ATTRIBUTE
    pi=3.14
    def __init__(self,radius=1):
        self.radius=radius
        self.area=radius * radius * Circle.pi
        #METHOD
    def get_circumference(self):
        return 2 * self.radius * self.pi
my_circle=Circle(10)
print(my_circle.get_circumference())
print(my_circle.area)
print(my_circle.radius)