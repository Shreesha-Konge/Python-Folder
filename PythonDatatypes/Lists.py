list=['One',2,'Three',4,'five']
print(list)
print(list[3]) #indexing
print(list[2:]) #slicing
another_list=['Six',7,'Eight']
new_list=list+another_list
print(new_list)
new_list.append('Nine') #to add new element w euse append()
print(new_list)
new_list[8]='Ten'
print(new_list) #mutable to change val
new_list[7:8]='Eleven','Twelve'
print(new_list)


