#FIBONACCI SERIES
max_number=int(input('Enter number : '))
a=0
b=1
fibonacci_sequence=[]
while a<max_number:
    fibonacci_sequence.append(a)
    a,b=b,a+b
print(f'Fibonacci series of numbers are : {fibonacci_sequence}')