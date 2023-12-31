#COMMON ELEMENTS IN BOTH LISTS
def my_lists(lst1,lst2):
    my_new_list=[]
    for i in lst1:
        if i in lst2:
            my_new_list.append(i)
    return my_new_list
lst1=[2,3,4,5,69,10]
lst2=[3,8,10,11,13,2]
my_new_list=my_lists(lst1,lst2)
print(f'Common elements in both lists are : {my_new_list}')