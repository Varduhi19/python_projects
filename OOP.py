# class cars:
#     def __init__(self, name, collor, prise):
#         self.name = name
#         self.collor = collor
#         self.prise=prise
        
#     def methot(self):
#         print(self.name, self.collor, self.prise)
        
# car1=cars('bnw', 'red', '10000')        
# car1.methot()
# car2=cars('bnw', 'blue', '10050')  
# car2.methot()


class BankAccount:
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
    def get_balance(self):
        print(self.balance)
    def deposit(self, amount):
        self.balance+=amount
        print(self.balance)
    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance-=amount
            print(self.balance)
        else:
            print("anbavarar mijocner")
owner1=BankAccount('Varduhi', 15000)
owner1.get_balance()
owner1.deposit(5000)
owner1.withdraw(26000)
owner1.withdraw(2000)

    
        