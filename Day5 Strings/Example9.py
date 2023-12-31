#REMOVE DUPLICATE CHAR FROM A STRING
def remove_dup(s):
    empty_str=' '
    for char in s:
        if char not in empty_str:
            empty_str+=char
            result=empty_str
    return result
s='Geeks for Geeks'
without_duplicates=remove_dup(s)
print(f'String without duplicates is : \n{without_duplicates}')
