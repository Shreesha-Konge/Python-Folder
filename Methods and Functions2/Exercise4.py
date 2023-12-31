def old_macdonald(name):
     if len(name)>3: 
        return  name[:3].capitalize() + name[3:].capitalize()
     else:
         return "Length is too Short"
name=input('Name is : ')
print(old_macdonald(name))

