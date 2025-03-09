import unittest

import bank
from bank import Bank


class TestBank(unittest.TestCase):
    def test_create_account(self):
        bank = Bank()
        account = bank.create_account("javiel", 1234, 100000)
        self.assertEqual(account.balance, 100000)
        account2 = bank.create_account("jeremy", 2345, 12334)
        self.assertEqual(account2.balance, 12334)

    def test_deposit_liability(self):
        bank = Bank()
        bank.create_account("javiel", 1234, 100000)
        bank.create_account("jeremy", 2345,12334)
        self.assertEqual(bank.deposit_liability(), 112334)


def test_find_accounts_by_name():
   pass





def test_find_account_by_number():
    bank = Bank()
    account1 = bank.create_account("111", "Alice", 500.0)
    account2 = bank.create_account("222", "Bob", 1000.0)
    found_account = bank.find_account_by_number("222")
    assert (found_account, account2)
    found_account = bank.find_account_by_number("111")
    assert (found_account, account1)




if __name__ == '__main__':
    unittest.main()
