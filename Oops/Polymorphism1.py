class Animal():
    def __init__(self,name):
        self.name=name
class Dog(Animal):
    def speak(self):
        print(self.name + ' says WOOF!')
class Cat(Animal):
    def speak(self):
        print(self.name + ' says MEOW!')
Dog1=Dog('Fido')
Cat1=Cat('Isis')
print(Dog1.speak())
print(Cat1.speak())

        