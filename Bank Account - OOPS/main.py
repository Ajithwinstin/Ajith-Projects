class BankAccount(object):
    defaultAccNumber = 1

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.accountNumber = BankAccount.defaultAccNumber
        BankAccount.defaultAccNumber = BankAccount.defaultAccNumber + 1

    def get_Account_details(self):
        # print(self.name)
        # print(self.accountNumber)
        return "Account Holder : {0} \nAccount Number : {1}".format(self.name, self.accountNumber)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print('Not enough Balance !')
        else:
            self.balance -= amount

    def getBalance(self):
        return self.balance


if __name__ == "__main__":
    myobj = BankAccount('Ajith', 50000)
    print(myobj.get_Account_details())
    myobj.deposit(15000)
    print(myobj.getBalance())
    myobj.withdraw(20000)
    print(myobj.getBalance())
