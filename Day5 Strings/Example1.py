#CONCATENATE INTO SINGLE STRING
def concatenate_str(my_lst):
    result_my_str=' '.join(my_lst)
    return result_my_str
my_lst=['This','is','a','list','of','words']
print(concatenate_str(my_lst))