#FACTORIAL PROGRAM
n=int(input('Enter a number : '))
factorial=1
if n<0:
    print('Sorry , there is no factorial for negative number ')
elif n==0:
    print('Factorial of 0 is : 1')
else:
    for i in range(1,n+1):
        factorial*=i
    print(f'Factorial of {n} is {factorial}')