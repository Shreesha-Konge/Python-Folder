def my_kwargs(**kwargs):
    print(kwargs)
print(my_kwargs(Fruit='Apple',Veggie='Potato'))
#using if else to know better
def my_kwargs_new(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My Favourite Fruit is {} '.format(kwargs['fruit']))
    else:
        print("I didn't like that fruit")
print(my_kwargs_new(fruit='Mango',Veggie='Aloooooo'))