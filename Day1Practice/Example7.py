my_str=input('Enter a string : ')
my_str=my_str.replace(' ','')
my_reverse_str=my_str[::-1]
if my_str==my_reverse_str:
    print('Palindrome')
else:
    print('Not a palindrome')
    