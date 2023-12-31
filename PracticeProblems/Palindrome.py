#Write a Python function that checks whether a word or phrase is 
#palindrome or not.
def palindrome(s):
    #To remove the replaces
    s=s.replace(' ','')
    #Reverse string and check if it's equal to original one
    #return (s == ''.join([c for c in reversed(s)]))
    return s==s[::-1]
print(palindrome('nurses run'))
