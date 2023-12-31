#COUNT THE OCCURENCES OF EACH ELEMENT IN A LIST
def count_elements(lst):
    words=[]
    for word in lst:
            count=lst.count(word)
            words.append((word,count))
    unique_elements=list(set(words))
    return unique_elements
lst=[1,2,2,3,4,5,5,5,5,6,6,7,8,9]
words=count_elements(lst)
print('Element occurences : ')
for word,count in words:
    print(f'{word},{count} times')