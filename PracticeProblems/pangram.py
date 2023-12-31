import string
def ispangram(str1,alphabet=string.ascii_lowercase):
    #Create a set of a alphaset
    alphaset=set(alphabet)
    #removing the spaces of a str1
    str1=str1.replace(' ','')
    #converting string into lowercase
    str1=str1.lower()
    #only considering unique values in a string
    str1=set(str1)
    #alphabet set=string set usr input
    return str1==alphaset
print(ispangram("The quick brown fox jumps over the lazy dog"))

    
