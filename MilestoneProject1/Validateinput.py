def user_choice():
    #INITIAL VARIABLES
    choice='WRONG'
    acceptable_range=range(0,10)
    within_range=False
    #DIGITAL AND WITHIN_RANGE CHECK
    while choice.isdigit() == False or within_range==False:
        choice=input('Please enter a number from (0-10): ')
        #Input Digit Check
        if choice.isdigit()==False:
            print('Sorry its not a digit!')
        #Range Check
        if choice.isdigit()==True:
            if int(choice) in acceptable_range:
                print('You entered correct input range : ' +str(choice))
                within_range = True
            else:
                print('Sorry you are out of acceptable range(10)!')
                within_range= False
    return int(choice)
print(user_choice())
