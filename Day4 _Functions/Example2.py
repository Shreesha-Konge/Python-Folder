#PALINDROME USING FUNCTION
def palindrome_func(my_string):
    my_string=my_string.replace(' ','')
    my_new_str=my_string[::-1]
    if my_string==my_new_str:
        print('PALINDROME')
    else:
        print('NOT A PALINDROME')
my_string=input('Enter a string : ')
print(palindrome_func(my_string))