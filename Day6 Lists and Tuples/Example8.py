#SORT BY THE LENGTH OF STRINGS
def sort_str(mylst):
    sorted_list=sorted(mylst,key=len)
    return sorted_list
mylst=['Shreesha','Pavani','Konge','Sai','Shree','Anu','Aditya']
#print(sort_str(mylst))
result=sort_str(mylst)
print('Sort by length: ')
for item in result:
    print(item)