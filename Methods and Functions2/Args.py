def myfunc(a,b):
    return sum((a,b)) * 0.05
print(myfunc(60,40))
#By using *args
def myfunc(*args):
    return sum(args)
print(myfunc(100,20,40,60))
def myfunc(*args):
    for item in args:
        print(item)
print(myfunc(100,20,30))
