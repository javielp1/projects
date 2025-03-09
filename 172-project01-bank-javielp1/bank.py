from bank_account import BankAccount


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, name, account_number, balance=0):
        account = BankAccount(name, account_number, balance)
        self.accounts.append(account)
        return account

    def deposit_liability(self):
        total_deposit_liability = sum(account.balance for account in self.accounts)
        return total_deposit_liability

    def find_account_by_number(self, account_number):
        for account in self.accounts:
            if account.acct_num == account_number:
                return account

    def find_account_by_name(self, name):
        for account in self.accounts:
            if account.name == name:
                return account



