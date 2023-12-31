#PANGRAM
import string
def pangram_sentence(my_str):
    alphabet=set(string.ascii_lowercase)
    my_str=my_str.replace(' ','')
    for char in alphabet:
        if char not in my_str:
            print('NOT PANGRAM')
            break
    else:
        print('PANGRAM')
my_str='The quick brown fox jumps over the lazy dog'
print(pangram_sentence(my_str))