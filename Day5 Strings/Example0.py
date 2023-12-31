#COUNT VOWELS IN STRING
def count_vowels(my_str):
    vowels=set('AEIOUaeiou')
    count=0
    for char in my_str:
        if char in vowels :
            count+=1
    return count
my_str=input('Enter a string : ')
num_vowels=count_vowels(my_str)
print('Number of vowels : ',num_vowels)