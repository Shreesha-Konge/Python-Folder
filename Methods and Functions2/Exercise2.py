#Write a function takes a two-word string and returns True if both
# words begin with same letter
def animal_crackers(text):
     word_list=text.split()
     return word_list[0][0]==word_list[1][0]
print(animal_crackers('Levelheaded Llama'))