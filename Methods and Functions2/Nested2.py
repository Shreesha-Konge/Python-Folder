x=50
def func(x):
    print(f'x is {x}')
    #LOCAL REASSIGNMENT ON A GLOBAL VARIABLE
    x='NEW VALUE'
    print(f'I just changed x value to {x}')
    return x
x=func(x)
print(x)