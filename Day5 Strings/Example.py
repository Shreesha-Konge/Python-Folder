#CHECKS PALINDROME
def palindrome_str(my_str):
    my_str=my_str.replace(' ','')
    my_new_str=my_str[::-1]
    if my_str==my_new_str:
        return f'PALINDROME --> {my_new_str}'
    else:
        return 'NOT A PALINDROME'
my_str=input('Enter a string : ')
print(palindrome_str(my_str))