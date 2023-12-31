mylist =[]
mystring ='HeyShree'
for letter in mystring:
    mylist.append(letter)
    print(mylist)
#List Comprehension
mystr2='Shreesha'
mylist1=[letter for letter in mystr2]
print(mylist1)
mylist2=[x for x in 'word']
print(mylist2)
mylist3=[num for num in range(0,10,2)]
print(mylist3)
mylist4=[num**2 for num in range(0,11)]
print(mylist4)
