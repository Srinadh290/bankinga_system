class Bank:
    def __init__(self,accno,name,balance=0):
        self.accno=accno
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(self.balance)
        else:
            print("deposited amount must be positive")
    def showbalance(self):
        print(self.balance)
class savingsaccount(Bank):
    def __init__(self, accno, name, balance=0):
        super().__init__(accno, name, balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("INValid operations because insufficient funds in your account")
        else:
            self.balance-=amount
            print(f"withdrawal amount is {amount},new balance {self.balance}")
class currentaccount(Bank):
    def __init__(self, accno, name, balance=0,limit=1000):
        super().__init__(accno, name, balance)
        self.limit=limit
    def withdrawal(self,amount):
        if amount > self.balance + self.limit:
            print("insufficient")
        else:
            self.balance-=amount
            print(f"withdrawal amount is {amount},new balance is {self.balance}")
saa=savingsaccount("sbi0909094103","sri",10000)
caa=currentaccount("4004123","akhii",3000000)
saa.deposit(10000)
saa.withdraw(2000)
saa.showbalance()
caa.deposit(1000)
caa.withdrawal(2500)
caa.withdrawal(1000)
caa.showbalance()
