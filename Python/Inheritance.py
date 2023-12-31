class Animal:
    def __init__(self):
        print('Animal was created ')
    def whoamI(self):
        print('Animal')
    def eat(self):
        print('Eating')
class Dog(Animal):
    def __init__(self):
         Animal.__init__(self)
         print('Dog was created')
    def whoamI(self):
        Animal.whoamI(self)
        print('Dog')
    def bark(self):
        print('Dog Barks')
d=Dog()
# d is an object of class dog.
print(d.whoamI())