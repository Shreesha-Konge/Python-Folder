class Animal():
    def __init__(self):
        print("Animal created")
    def who_am_I(self):
        print("I am an Animal")
    def eat(self):
        print("I am Eating")
my_animal=Animal()
class Dog(Animal):
    def __init__(self):
        #Animal.__init__(self)
        print('Dog Created')
    def bark(self):
        print('Woof!')
    def eat(self):
        print('I am a Dog and am a Animal')
my_dog=Dog()
print(my_dog.bark())
print(my_dog.who_am_I())
print(my_dog.eat())
