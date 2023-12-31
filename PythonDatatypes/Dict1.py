new={'k1':['a','b','c','d','e']}
print(new)
list=new['k1']
print(list)
list.pop()
print(list)
letter=list[3]
print(letter)
caps=letter.upper()
print(caps)
#one step of changing 'c' to caps
list1=new['k1'][3].upper()
print(list1)
