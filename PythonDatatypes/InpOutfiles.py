
with open('my_new_file.txt',mode='r') as f:
    read1=f.read()
    print(read1)
#to read a file
with open('my_new_file.txt',mode='a') as f:
    write1=f.write('\nFour on Fourth')
    print(write1)
with open('my_new_file.txt',mode='r') as f:
    read2=f.read()
    print(read2)
    #a is append to add val
with open('Introfile.txt',mode='w') as f:
    print(f.write('Hey , I am Konge Sai Shreesha'))
with open('Introfile.txt',mode='r') as f:
    print(f.read())