#REMOVE VOWELS IN A STRING
def remove_vow(s):
    empty_str=' '
    vowels='AEIOUaeiou'
    for char in s:
        if char not in vowels:
            empty_str+=char
            res = empty_str
    return res
s=input('Enter a String : ')
result=remove_vow(s)
print(f'A string without vowels is : {result}')
