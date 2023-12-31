list1=[]
for x in [2,4,6]:
    for y in [1,10,100]:
        list1.append(x*y)
print(list1)
#By using List Comprehension
list2=[(x*y) for x in [2,4,6] for y in [1,10,100]]
print(list2)