import pytest
from bank_account import BankAccount


def test_check_balance_and_deposit():
    acct = BankAccount(12345, "javiel")
    acct.deposit(101)
    assert acct.check_balance() == 101

    acct2 = BankAccount(13244, "Bar")
    assert acct2.check_balance() == 0
    acct2.deposit(10)
    with pytest.raises(ValueError):
        acct2.deposit(-10)


def test_withdraw():
    acct = BankAccount(10020, "javiel")
    acct.deposit(100)
    acct.withdraw(50)
    assert acct.check_balance() == 50

    acct2 = BankAccount(2005, "green")
    acct2.deposit(500)
    acct2.withdraw(501)
    assert acct2.check_balance() == -1
    with pytest.raises(ValueError):
        acct2.withdraw(501)


def test_get_transaction_history():
    acct = BankAccount(10100, "john")
    acct.deposit(100)
    acct.withdraw(25)
    transactions = acct.get_transaction_history()
    assert (transactions, [("deposit", 100), "withdraw", 25])

    acct2 = BankAccount(99999, "lucas")
    acct2.deposit(1000)
    acct2.withdraw(890)
    transactions = acct2.get_transaction_history()
    assert (transactions, [("deposit", 1000), "withdraw", 890])

def test_transfer():
    acct = BankAccount(28392,"JAIELL")
    acct.deposit(100)
    acct2 = BankAccount(38299,"john")
    acct.transfer(acct2,100)
    assert acct2.check_balance() == 100