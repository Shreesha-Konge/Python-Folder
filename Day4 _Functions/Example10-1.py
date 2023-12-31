def multiple_table(num):
    for i in range(1,11):
        result=num*i
        print(f'{num} X {i} = {result}')
num=int(input('Enter a  number : '))
print(multiple_table(num))