#sum of positive integers
mylist=[1,-2,-3,8,9,10,-11]
result=0
for num in mylist:
    if num>0:
        result+=num
print(result)