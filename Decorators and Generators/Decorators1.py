def hello(name='Sai'):
    print('Iam a hello() function!!')
    print('Hello ' +name)
    def greet():
        return '\t This is a greet() inside hello() function'
    def welcome():
        return '\t This is a welcome() inside hello() function!'
    #print(greet())
    #print(welcome())
    if name=='Sai':
        return greet()
    else:
        return welcome()
print('I am an end of the function()')
my_new_func = hello
print(my_new_func())
