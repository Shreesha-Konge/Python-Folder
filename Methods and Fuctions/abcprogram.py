def greatest_num(a,b,c):
    if a>b and a>c:
        print('a is greater')
    elif b>c and b>a:
        print('b is greater')
    else:
        print('c is greater')
a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
c=int(input('Enter third number: '))
greatest_num(a,b,c)