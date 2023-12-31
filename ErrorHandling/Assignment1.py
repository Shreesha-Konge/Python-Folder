try:
    for i in ['a','b','c']:
       print(i**2)
except TypeError:
    print('There is an Type Error')
except:
    print('Whooops! Str cannot concatenate with int')




