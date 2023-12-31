def my_args_kwargs_func(*args,**kwargs):
    print('My Fav Food is {} and cost is {} rupees '.format(kwargs['Food'],args[0]))
    print(f'My Fav Fruit is {kwargs["fruit"]} and cost is {args[1]}')
print(my_args_kwargs_func(30,50,60,Food='Dosa',fruit='Mango'))
#second example
def myfunc(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        #print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
        print(f"I like {args[0]} and my favorite fruit is {kwargs['fruit']}")
    else:
        pass
myfunc('eggs','spam',fruit='cherries',juice='orange')