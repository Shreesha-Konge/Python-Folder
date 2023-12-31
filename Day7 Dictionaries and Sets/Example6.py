#COUNT THE NUMBE ROF OCCURENCES OF EACH CHAR IN STRING
def total_count_char(input_str):
    char_count={}
    for char in input_str:
        #check the str for spaces,numbers
        if char.isalpha():
            char=char.lower()
            if char not in char_count:
                char_count[char]=1
            else:
                char_count[char]+=1
    return char_count
input_str='Hello, World'
result=total_count_char(input_str)
for char,count in result.items():
    print(f"'{char}':{count}")

