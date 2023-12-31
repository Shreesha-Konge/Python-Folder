#maximum length of words
def max_len_of_word(my_lst):
    max_length=0
    max_word=' '
    for word in my_lst:
        if len(word)>max_length:
            max_word=word
            max_length=len(word)
    print(f'Maximum length of word is {max_length}')
    print(f'Longest word is {max_word}')
my_lst=['Shreesha','Abhimanyu','Akshara','Pav','Bhii']
longest_word=max_len_of_word(my_lst)
print(longest_word)
