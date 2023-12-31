from random import shuffle
#Creating a new list to find 'O'
mynewlist=[' ','O',' ']
def shuffle_list(mynewlist):
     shuffle(mynewlist)
     return mynewlist
#Checking for shuffle_list function working
print(shuffle_list(mynewlist))
#Asking user to guess the index position
def player_guess():
     guess=''
     while guess not in ['0','1','2']:
          guess=input('Please pick an index position from 0,1,2 : ')
     return int(guess)
print(player_guess())  
#Functions to interact each other
def check_guess(mynewlist,guess):
     if mynewlist[guess] == 'O':
          print('Correct Guess!')
     else:
          print('Wrong Guess!!!!')
          print(mynewlist)  
#INTIAL LIST
mynewlist=[' ','O',' ']
#SHUFFLE THE LIST USING shuffle_list function
mixedup_list=shuffle_list(mynewlist)
#GUESS the user using player_guess function
guess=player_guess()
#CHECK IF GUESS IS CORRECT OR WRONG AND PRINT IT OUT
print(check_guess(mixedup_list,guess))
     