#multiplication table of  a number
number=int(input('Enter a number which you want to multiply : '))
count=0
while count<10:
    count+=1
    print(number,'X',count,'=',number*count)