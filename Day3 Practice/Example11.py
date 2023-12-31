#PRIME NUMBERS FROM 1 TO 50
def prime_num(start,end):
    for i in range(start,end+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
start=int(input('Enter a start range : '))
end=int(input('Enter an end range : '))
print(prime_num(start,end))    