#LENGTH OF LONGEST WORD
def word_len(my_sen):
    words=my_sen.split()
    longest_len=0
    for word in words:
        word_length=len(word)
        if word_length>longest_len:
            longest_len=word_length
            longest_word=word
    return longest_word,longest_len
my_sen='hey am sai shreesha konge'
longest_word,longest_len=word_len(my_sen)
print(f'Longest Word is : {longest_word}')
print(f'Length of word is : {longest_len}')
