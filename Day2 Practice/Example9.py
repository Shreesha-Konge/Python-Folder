#count no of vowels in a string
def count_vowels(input_str):
    count=0
    vowels=set('AEIOUaeiou')
    for char in input_str:
        if char in vowels:
            count+=1
    return count
input_str=input('Enter a string : ')
print(count_vowels(input_str))

