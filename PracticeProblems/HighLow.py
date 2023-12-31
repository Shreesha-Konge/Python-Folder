#Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    #if num >= low and num <= high:
    if num in range(low,high):
        return f'{num} is in the range between {low} and {high} '
       #return True
    else:
        return 'not in range'
num=int(input('Enter number : '))
low=int(input('Enter lowest number :'))
high=int(input('Enter highest number:'))
print(ran_check(num,low,high))