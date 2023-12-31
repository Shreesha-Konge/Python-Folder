#MULTIPLICATION TABLE USING FUNCTION
def mul_table(num):
    count=1
    while count<=10:
        result=num * count
        print(f'{num} X {count} = {result}') 
        count+=1
num=int(input('Enter number : '))
print(mul_table(num))