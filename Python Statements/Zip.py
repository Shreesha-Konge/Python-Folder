mylist1=[1,2,3,4,5]
mylist2=['a','b','c','d','e']
for i in zip(mylist1,mylist2):
    print(i)
l1=[100,200,'Sai']
l2=[500,'Shree']
l3=[1,2,3,4,5,6,7]
my_zip_function=zip(l1,l2,l3)
for item in my_zip_function:
    print(item)
#tuple unpacking
for a,b in zip(mylist1,mylist2):
    print(b)
