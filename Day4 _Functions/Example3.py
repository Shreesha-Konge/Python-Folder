#FACTORIAL
def factorial_num(n):
    if n==0:
        return 1
    else:
        return n * factorial_num(n-1)
n=int(input('Enter a number : '))
print(factorial_num(n))
