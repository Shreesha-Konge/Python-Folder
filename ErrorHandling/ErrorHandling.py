try:
    f=open('testfile','r')
    f.write('Write a test file')
except TypeError:
    print('There is an error in Typing')
except OSError:
    print("Error in OS")
else:
    print('Successfully written a file')
finally:
    print('I always execute')