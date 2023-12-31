class Electronics:
    def __init__(self,model,price):
        self.model=model
        self.price=price
    def display(self):
        return f'Model:{self.model} and Price:{self.price}'
class Phone(Electronics):
    def __init__(self, model, price):
        super().__init__(model, price)
    def display_phone(self):
        parent_info=super().display()
        return parent_info
class Laptop(Electronics):
    def __init__(self, model, price):
        super().__init__(model, price)
    def display_laptop(self):
        parent_info=super().display()
        return parent_info
phone=Phone('16A',20000)
laptop=Laptop('I5',45000)
print(phone.display_phone())
print(Laptop.display_laptop())
