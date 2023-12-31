#COUNT THE NO OF WORDS WITH MORE THAN 5 CHAR
s=['Shreesha','Sai','Konges','Abhiram','Adeppa','Pavani']
count=0
for i in s:
    if len(i)>5:
       count+=1
print(f'The number of words is {count}')

