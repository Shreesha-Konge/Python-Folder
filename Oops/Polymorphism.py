class Dog():
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(self.name + ' says WOOF!')
class Cat():
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(self.name + ' says MEOW!')
my_dog=Dog('Niko')
my_cat=Cat('Felix')
print(my_dog.speak())
print(my_cat.speak())
for pet in [my_dog,my_cat]:
    print(pet.speak())
def pet_name():
    print(pet.speak())
        