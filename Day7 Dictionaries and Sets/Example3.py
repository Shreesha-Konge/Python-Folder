#FUNCTION REMOVES A KEY-VALUE PAIR
def removes_key_value_pair(d,key_to_remove):
    if key_to_remove in d:
        removed_value=d.pop(key_to_remove)
        return removed_value
    else:
        return None
d={'a':1,'b':2,'c':3,'d':4}
key_to_remove='b'
removed_value1=removes_key_value_pair(d,key_to_remove)
if removed_value1 is not None:
    print(f'Removed Key-Value Pair is : {key_to_remove}:{removed_value1}')
else:
    print(f'Key {key_to_remove} not found in dictionary')
print(f'Updated dictionary is : {d}')


    