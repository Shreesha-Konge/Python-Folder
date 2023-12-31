class Dog():
    def __init__(self, name):
        self.name=name
    def speak(self):
        return self.name + 'Bow Bow'
class Cat():
    def __init__(self, name):
        self.name=name
    def speak(self):
        return self.name + 'Meow Meow'
d=Dog('Doggy says  ')
c=Cat('Catty says  ')
print(d.speak())
print(c.speak())