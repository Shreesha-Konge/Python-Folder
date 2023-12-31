#COUNT NO OF WORDS FROM A SENTENCE
def count_words(s):
    count=0
    s=s.split()
    count=len(s)
    return count
s=input('Enter a sentence : ')
total_wordcount=count_words(s)
print(f'Total count of words : {total_wordcount}')