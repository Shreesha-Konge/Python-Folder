#PRINT UNIQUE NAMES BY REMOVING DUPLICATES
def unique_names(my_lst):
    my_new_list=[]
    for word in my_lst:
        if word not in my_new_list:
            my_new_list.append(word)
    return f'UNIQUE ELEMENTS : {my_new_list}'
my_lst=[1,2,2,5,5,5,6,7,8,9,9,9,10]
print(unique_names(my_lst))
