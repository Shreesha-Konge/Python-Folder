#second method
def old_macdonald1(name):
    first_letter=name[0]
    betweenpart=name[1:3]
    fourth_letter=name[3]
    rest=name[4:]
    return first_letter.upper()+betweenpart+fourth_letter.upper()+rest
print(old_macdonald1('macdonald'))