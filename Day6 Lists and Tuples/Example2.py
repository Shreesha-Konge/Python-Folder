#LARGEST AND SMALLEST ELEMENTS IN A LIST
def largest_smallest(my_lst1):
    largest_num=max(my_lst1)
    smallest_num=min(my_lst1)
    print(f'Largest number is : {largest_num}')
    print(f'Smallest number is : {smallest_num}')
my_lst1=[19,10,14,16,20,10,25,8]
print(largest_smallest(my_lst1))
