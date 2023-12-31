#To display the list
game_list=[0,1,2]
def display_game(game_list):
    print('Here is the current list : ')
    print(game_list)
print(display_game(game_list))
#To take pick a position
def position_choice():
    choice='WRONG'
    while choice not in ['0','1','2']:
        choice=input('Please pick a position (0,1,2) : ')
        if choice not in ['0','1','2']:
            print('Sorry , Invalid choice!')
    return int(choice)
print(position_choice())
#To replace a position from diigit to string
def replacement_choice(game_list,position):
    user_placement=input('Type a string to place a position: ')
    game_list[position]=user_placement
    return game_list
print(replacement_choice(game_list,1))
#Game on Y or N
def gameon_choice():
    choice='WRONG'
    while choice not in ['Y','N']:
        choice=input('Do you want to keep playing ? (Y or N) : ')
        if choice not in ['Y','N']:
            print("Sorry I don't understand , please select Y or N")
    if choice =='Y':
        return True
    else:
        return False
print(gameon_choice())
#Final Result
game_on=True
game_list=[0,1,2]
while game_on==True:
    display_game(game_list)
    position=position_choice()
    Updated_game_list=replacement_choice(game_list,position)
    display_game(Updated_game_list)
    game_on=gameon_choice()