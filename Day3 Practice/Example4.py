#Store even numbers in new list
numbers_list=[10,20,22,23,25,67,89,52,90,13,12]
my_new_list=[]
for num in numbers_list:
    if num%2==0:
        my_new_list.append(num)
print(my_new_list)