#Given a string, return a string where for every character in the 
#original there are three characters
def paper_doll(text):
    result=' '
    for char in text:
        result += char*3
    return result
text=input('Enter a text ')
print(paper_doll(text))