def count_primes(num):
    #less than 2 logic
    if num <2 :
        return 0
    #storing nums in list starts with 2
    primes=[2]
    #counter going upto input number
    x=3
    while x<=num:
        #for y in range(3,x,2):
        for y in primes:
            if x%y==0:
                x+=2
                break
        else:
            primes.append(x)
            x+=2
    print(primes)
    return len(primes)
print(count_primes(100))

