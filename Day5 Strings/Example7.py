#REVERSE THE SENTENCE IN REVERSE ORDER
def reverse_sentence(s):
    s=s.split()
    s=s[::-1]
    result=' '.join(s)
    return result
s='Hey am shree konge'
reversed_result=reverse_sentence(s)
print(f'Reversed sentence is : \n{reversed_result}')