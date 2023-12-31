def check_even(num):
    return num%2==0
mynums=[1,2,3,4,5,6]
print(list(filter(check_even,mynums)))
#or else we can use for 
for i in filter(check_even,mynums):
    print(i)