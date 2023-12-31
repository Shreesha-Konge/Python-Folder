#PRODUCT DATA
class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def display(self):
        return f'Name:{self.name}\nPrice:{self.price}\nQuantity{self.quantity}'
product_data=Product('Chocolate',250,100)
print(product_data.display())
        