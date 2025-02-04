class Account:
    def __init__(self,owner,balance,):
        self.owner=owner
        self.balance=balance
    
    
    def withdraw(self, withdraw_amount):
        if (self.balance-withdraw_amount)>0:
            self.balance-=withdraw_amount
            return f'BankAccount(owner={self.owner}, balance={self.balance}$)'

        else:
            return "you do not such amount of money "
    def deposite(self, deposite_amount):
        if (self.balance-deposite_amount)>0:
            self.balance-=deposite_amount
            return f"Deposited={deposite_amount}$, Remained={self.balance}$ "
        else:
            return "you do not such amount of money to do so"
Darkhan=Account("Darkhan",1000)
print(Darkhan.withdraw(400))
print(Darkhan.deposite(400))
print(Darkhan.withdraw(400))
