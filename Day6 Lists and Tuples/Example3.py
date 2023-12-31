#SQUARED LIST
def squared_lst(my_lst):
    new_lst=[]
    for i in my_lst:
        i=i**2
        new_lst.append(i)
    return new_lst
my_lst=[2,4,8,9,10,13,15]
print(squared_lst(my_lst))
