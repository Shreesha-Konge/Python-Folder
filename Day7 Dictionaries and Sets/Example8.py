#SORT ON A SPECIFIED KEY
def list_of_dict(mylist):
    sorted_list=sorted(mylist,key=lambda x:x[key_to_be_sort])
    return sorted_list
mylist=[
    {'name':'Alice','score':90},
     {'name':'Sai','score':75},
     {'name':'Pari','score':80}
]
key_to_be_sort='score'
print(list_of_dict(mylist))