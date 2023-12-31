def hello():
    print('Hello Shree')
def other(some_other_func):
    print('Other codes will execute here!!')
    print(some_other_func())
print(hello())
print(other(hello))