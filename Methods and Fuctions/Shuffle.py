examplelist=[1,2,3,4,5,6,7,8,9,10]
from random import shuffle
shuffle(examplelist)
print(examplelist)
#In order to store and save the result we use functions
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
result=shuffle_list(examplelist)
print(result)