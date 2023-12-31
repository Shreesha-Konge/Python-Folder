#list of names start with 'A'
names_list=['Anuradha','Singh','Abhi','Anugrah','Shree','Pav']
my_A_list=[]
for i in names_list:
    #if i[0]=='A':
     if i.startswith('A'):
        my_A_list.append(i)
print(my_A_list)


