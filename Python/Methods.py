class Circle:
    pi=3.14
    def __init__(self,radius=3):
        self.radius=radius
        self.area=radius*radius*Circle.pi
        #area=r*r*pi
    def getRadius(self,new_radius):
        self.radius=new_radius
        self.area=new_radius*new_radius*self.pi
        #circumference =2*pi*r
    def getCircumference(self):
         return 2*self.pi*self.radius
c=Circle()
#default radius is set to one
print('Radius is ' , c.radius)
print('Area is ' , c.area)
print('Circumference is ' , c.getCircumference())