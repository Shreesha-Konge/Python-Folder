#count names start with vowel
def count_vow(my_lst):
    vowels='AEIOUaeiou'
    count=0
    for i in my_lst:
        if i[0] in vowels :
            count+=1
    return count
my_lst=['Shree','Anu','Abhi','Oner','uma','vishnu','Ilias']
word_count=count_vow(my_lst)
print(f'Total words start with vowel : {word_count}')
