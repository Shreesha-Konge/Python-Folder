#Write a Python function that accepts a string and calculates the 
#number of upper case letters and lower case letters.
def up_low(s):
    upper=0
    lower=0
    for c in s:
        if c.isupper():
            upper+=1
        elif c.islower():
            lower+=1
        else:
            pass
    print('Orginal String : ',s)
    print('No of upper case characters : ',upper)
    print('No of lower case characters : ',lower)
s='Hello Mr. Rogers, how are you this fine Tuesday?'
print(up_low(s))