#Dictionary of highest value
lists_of_dicts = [
     {'name':'Alice','score':90},
     {'name':'Sai','score':75},
     {'name':'Pari','score':80}
]
key_to_max='score'
max_dic=max(lists_of_dicts,key=lambda x:x[key_to_max])
print(max_dic)
