class Account:
    def __init__(self,balance,account_no):
        self.__balance=balance
        self.__account_no=account_no
    def debit(self,amount):
        self.__balance-=amount
        print(f"rs{amount} was debited")
    def credit(self,amount):
        self.__balance+=amount
        print(f"rs{amount} was credited")
    def get_balance(self):
        print(f"balance:{self.__balance}")
acc1=Account(10000,1234567)
acc1.debit(5000)
acc1.credit(10000)
acc1.get_balance()
