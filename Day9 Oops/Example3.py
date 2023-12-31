#BASIC BANK ACCOUNT
class Bank_Account:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            return f'Amount Deposited:{amount} & Balance:{self.balance}'
        else:
            return 'Invalid amount'
    def withdraw(self,amount):
        if amount>0 and amount<=self.balance:
            return f'Withdraw Amt:{amount} & Balance:{self.balance}'
    def get_balance(self):
        return f'Account Balance for {self.account_holder}:{self.balance}'
B=Bank_Account('Shree',25000)
print(B.deposit(500))
print(B.withdraw(550))
print(B.get_balance())