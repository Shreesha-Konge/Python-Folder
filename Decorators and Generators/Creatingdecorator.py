#Creating a Decorator
def new_decorator(func):
    def wrap_func():
        print("Code would be here, before executing the func")
        func()
        print("Code here will execute after the func()")
    return wrap_func
def func_needs_decorator():
    print("This function is in need of a Decorator")
#REASSIGN A VARIABLE
func_needs_decorator = new_decorator(func_needs_decorator)
print(func_needs_decorator())
#@new_dec we are using here
@new_decorator
def new_original_func():
    print('I am a original function and needs decorator')
print(new_original_func())