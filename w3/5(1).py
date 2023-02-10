#Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn
class Account:
    def __init__(self, owner, balance):
        self.owner = str(owner)
        self.balance = int(balance)
    def deposit(self):
        dep = int(input())
        self.balance += dep
    def withdraw(self):
        wit = int(input())
        if wit <= self.balance:
            self.balance -= wit
        else:
            print('Insufficient funds!')

owner = input()
balance = input()
my = Account(owner, balance)
my.deposit()
print(my.balance)
my.withdraw()
print(my.balance)
