myfile=open('myfile.txt')
print(myfile.read())
#To read it again we use seek , it comes ar=t 0 index and start read again
myfile.seek(0)
print(myfile.read())
with open ('myfile.txt') as my_new_file:
    contents=my_new_file.read()
    print(contents)