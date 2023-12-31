def ask():
    waiting=True
    while  waiting:
        try:
            num=int(input('Please provide an integer : '))
            result=num **2
            print(result)
        except:
            print('An error occurred! Please try again! \n')
            continue
        else:
            print('Thank you, your number squared is: ' +str(result))
            waiting=False
print(ask())