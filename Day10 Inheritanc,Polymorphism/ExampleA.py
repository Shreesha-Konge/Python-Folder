class Animal:
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return 'Woof!'
class Cat(Animal):
    def sound(self):
        return 'Meow!'
dog=Dog()
cat=Cat()
print(dog.sound())
print(cat.sound())