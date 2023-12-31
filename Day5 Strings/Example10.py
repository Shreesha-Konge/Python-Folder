#WORD AND SENTENCE , IF WORD IS PRESENT IN SENTENCE
def word_sentence(sentence,word):
        if word in sentence:
            return f'{word}' 
        else :
            return False
sentence=input('Enter a sentence : ')
word=input('Enter a word : ')
word_in_sentence=word_sentence(sentence,word)
print(f'Word in Sentence : {word_in_sentence}')