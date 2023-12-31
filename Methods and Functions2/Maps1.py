def slicer(mystring):
    if len(mystring)%2==0:
        return 'EVEN'
    else:
        return mystring[0]
names=['Andy','Shreeeshaaa','Sai']
for item in map(slicer,names):
       print(item)
print(list(map(slicer,names)))
