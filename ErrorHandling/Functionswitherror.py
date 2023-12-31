def input_number():
    while True:
        try:
            result=int(input('Please provide an integer number!'))
            print(result)
        except:
            print('Whoops! its not an integer!')
            continue
        else:
            print('Added an Integer ' +str(result))
            break
        finally:
            print('I will always execute')
print(input_number())