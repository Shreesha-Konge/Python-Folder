#REVERSES A STRING
def reverse_str(my_str):
    result_str=my_str[::-1]
    return result_str
my_str=input('Enter a string : ')
print(reverse_str(my_str))