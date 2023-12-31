list1=[x for x in range(0,11) if x%2==0 ]
print(list1)
l2=[x**3 for x in range (0,6) if x%2==0]
print(l2)
#To get Farhenheit value
celsius=[0,10,20,34.5]
Farhenheit=[((9/5) * temp +32) for temp in celsius]
print(Farhenheit)
#To get Farhenheit value by using for loop
celsius=[0,10,20,34.5]
Farhenheit=[]
for temp in celsius:
    Farhenheit.append((9/5) * temp +32)
    print(Farhenheit)