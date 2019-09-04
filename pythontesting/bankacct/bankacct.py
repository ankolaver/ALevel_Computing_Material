class BankAccount:

    def __init__(self, acctno, balance):
        self.acctno = acctno
        self.balance = balance

    def deposit(self,amt):
        self.balance+=amt
        return self.balance

    def withdraw(self,amt):
        self.balance -= amt
        return self.balance

    def display(self):
        print(self.accntno)
        print(self.balance)

    def calc_interest(self,year):
        self.balance = int(self.balance*((1.02)**year))
        return self.balance
