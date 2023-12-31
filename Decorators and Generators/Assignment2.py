#import random
#random.randint(1,10)
from random import randint
randint(1,10)
def rand_num(low,high,n):
    for n in range(n):
        yield randint(low,high)
        #yield random.randint(low,high)
    return n
for num in rand_num(1,10,12):
    print(num)

