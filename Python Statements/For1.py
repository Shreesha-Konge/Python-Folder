mylist1=[1,2,3,4,5,6,7,8,9,10]
for num in mylist1:
    if(num%2==0):
        #print('Even Number is ' +str(num))
        print('Even Number is {}'.format(num))
    else :
        print(f'Odd number is {num}')