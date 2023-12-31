class Dog():
    species='mammal'
    def __init__(self,breed,name,spots):
        self.mybreed=breed
        self.myname=name
        self.myspots=spots
    def bark(self,number,location):
        print('My name is {} and number is {} and loc is {} '.format(self.myname,number,location))
#INSTANCES
my_dog=Dog(breed='Huskie',name='Oggy',spots='NO SPOTS')
print(my_dog.mybreed)
print(my_dog.myname)
print(my_dog.myspots)
print(my_dog.species)
print(my_dog.bark(10,'Banglore'))