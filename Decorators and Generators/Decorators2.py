def cool():
    def super_cool():
        return 'Iam super cool!!'
    
    return super_cool
my_func=cool()
print(my_func())