class Account():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def __str__(self):
        return f'Account Owner : {self.owner}\nAccount Balance : {self.balance}'
    def deposit(self,amount):
        self.balance= self.balance+amount
        print(f'Deposit Accepted : {amount}')
    def withdraw(self,amount):
        if self.balance>=amount:
           print(f'Withdraw Accepted : {amount}')
           self.balance= self.balance-amount 
        else:
            print('Funds Unavailable')
A=Account('Jose',100)
print(A)
print(A.deposit(50))
print(A.withdraw(150))
print(A)

        