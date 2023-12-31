#Given a sentence, return a sentence with the words reversed
def master_yoda(text):
     return ' '.join(text.split()[::-1])
text='Iam the best'
print(master_yoda(text))    