def hello(name='Shree'):
    print('I am a hello() function!!')
    print('Hello ' +name)
greet=hello
print(greet())
del hello
#HELLO FUNC WILL GET DELETED IF WE TRY TO EXXECUTE IT WON'T GET EXECUTED
print(greet())
