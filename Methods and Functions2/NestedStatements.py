#GLOBAL
name='Hey am a Global variable'
def greet():
    #ENCLOSING FUNCTION LOCAL
    name='Sammy'
    def hello():
        #LOCAL
        #name='Hey am a Local variable'
        print(f'Hello {name}')
    print(hello())
print(greet())