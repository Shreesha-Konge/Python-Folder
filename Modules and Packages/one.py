def func():
    print('FUNC() is in ONE.PY')
print('Top Level one.py')
if __name__=='__main__':
    print('ONE.PY is being run directly')
else:
    print('ONE.PY has been imported')