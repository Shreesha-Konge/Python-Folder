#Palindrome
string=input('Enter a string : ')
string=string.replace(' ','').lower()
if string==string[::-1]:
    print('String is palindrome')
else:
    print('String is not a palindrome')


