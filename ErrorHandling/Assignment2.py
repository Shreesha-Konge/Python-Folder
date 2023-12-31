try:
    x = 5
    y = 0
    z = x/y
    print(f'Val of z is {z}')
except ZeroDivisionError:
    print('Cannot divide by zero')
except:
    print('Any number cannot divide by zero')
finally:
    print('All Done')
