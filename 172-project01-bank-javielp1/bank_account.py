class BankAccount:

    def __init__(self, acct_number: object, name: object, balance = 0):
        self.acct_num = acct_number
        self.name = name
        self.balance = balance
        self.transaction_history = []

    def check_balance(self):
        return self.balance

    def deposit(self, dep_amount):
        if dep_amount <= 0:
            raise ValueError("Amount must be greater than 0")
        self.balance = self.balance + dep_amount

    def withdraw(self, dep_amount):
        if self.balance < dep_amount or 0 > dep_amount:
            raise ValueError("Amount must be less than or equal to the account balance")
        self.balance = self.balance - dep_amount
        return self.balance

    def __str__(self):
        return " Current Balance: " + str(self.balance)

    def get_transaction_history(self):
        return self.transaction_history

    def transfer(self,acct1, amount):
        if self.check_balance() > amount:
            raise ValueError("Amount must be greater than")
        self.withdraw(amount)
        acct1.deposit(amount)






