#AREA OF TRIANGLE
def area_of_triangle(b,h):
    area=(1/2)* b * h
    return area
b=int(input('Enter Base : '))
h=int(input('Enter height : '))
print(area_of_triangle(b,h))