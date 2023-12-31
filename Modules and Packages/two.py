import one
print('TWO.PY is TOP Level')
print(one.func())
if __name__=='__main__':
    print('TWO.PY is being run directly')
else:
    print('TWO.PY has being imported')
