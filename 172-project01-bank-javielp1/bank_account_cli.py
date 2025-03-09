from bank_account import BankAccount


def bank_account_cli(the_account):
    """
    a function to allow the user to interact with a bank account, seeing the account info,
    repeatedly choosing an operation to do, seeing the resulting change to the account info, and being able to quit
    :param the_account: the BankAccount that the user will interact with
    :post: the account has any number of transactions performed by the user through the cli
    """
    while True:

        interact = input(f"would you like to w, d,check the transaction history or break for {the_account}?")
        match interact:

            case "W":
                withdraw_cli(the_account)
            case "w":
                withdraw_cli(the_account)
            case "D":
                deposit_cli(the_account)
            case "d":
                deposit_cli(the_account)
            case "transaction ":
                get_transaction_cli(the_account)
            case "break":
                break

            case _:
                print("invalid input")

    # Here you should loop: printing info, asking the user for a command, calling deposit_cli or withdraw_cli when
    # necessary, or doing other commands as necessary


def deposit_cli(the_account):
    """
    a function to allow the user to complete a deposit. The user should be able to enter an amount of money,
    and they will be told whether the deposit was successful or not and why
    :param the_account: the BankAccount that the deposit will affect
    :post: the account has a higher balance if the deposit was valid, and the user is informed of success/failure
    """
    user = input("Please enter your amount to deposit")
    user = int(user)
    try:
        the_account.deposit(user)
        print(f"succesfully deposited {user}")
    except:
        print("invalid input")







def withdraw_cli(the_account):
    """
    a function to allow the user to complete a withdrawal. The user should be able to enter an amount of money,
    and they will be told whether the withdrawal was successful or not and why
    :param the_account: the BankAccount that the withdrawal affect
    :post: the account has a lower balance if the withdrawal was valid, and the user is informed of success/failure
    """
    user = input("Please enter your amount to withdraw")
    user = int(user)
    try:
        the_account.withdraw(user)
        print(f"Your withdraw amount of {user} was successful")
    except:
        print("invalid input")


def get_transaction_cli(the_account):
    return the_account.get_transaction_history()


def main():
    example_account = BankAccount(123, "Toby", 300)
    bank_account_cli(example_account)


if __name__ == "__main__":
    main()
