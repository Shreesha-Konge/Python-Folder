def unique_lists(lst):
    x=[]
    for number in lst:
        if number not in x:
            x.append(number)
    return x
lst=[1,1,1,2,2,3,3,4,5]
print(unique_lists(lst))