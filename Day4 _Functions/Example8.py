#TWO LISTS AND RETURNS THEIR INTERSECTION
def intersection_func(mylst1,mylst2):
    mylst3=[]
    for item in mylst1:
        if item in mylst2:
            mylst3.append(item)
    return mylst3
mylst1=[1,2,3,4,5,6,7,8]
mylst2=[2,3,9,10,11,4,5,12]
result=intersection_func(mylst1,mylst2)
print(result)
