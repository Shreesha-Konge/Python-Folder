def even_odd_func(num):
    if num %2==0:
        return 'even'
    else:
        return 'odd'
num=int(input('Enter a number : '))
print(even_odd_func(num))
