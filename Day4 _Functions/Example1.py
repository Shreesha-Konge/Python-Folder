#LIST OF POSITIVE INTEGERS USING FUNCTIONS
def sum_of_num(numbers_list):
    result=0
    for n in numbers_list:
        if n>0:
            result+=n
    return result
numbers_list=[10,-20,40,50,98,-7,-9]
Total=sum_of_num(numbers_list)
print(f'The sum of postive integers is : {Total}')
