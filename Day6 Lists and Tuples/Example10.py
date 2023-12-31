#UNIQUE ELEMENTS IN BOTH LISTS
def unique_elements(lst1,lst2):
    lst3=[]
    for element in lst1:
        if element in lst2:
            lst3.append(element)
    return f'Common elements : {lst3}'
lst1=[1,2,3,4,5,6,7,8,9]
lst2=[9,2,3,4,10,19,12]
print(unique_elements(lst1,lst2))