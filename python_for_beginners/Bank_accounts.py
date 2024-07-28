class BalanceException(Exception):
    pass

class Bank_Account():
    def __init__(self, initial_balance, user_name):
        self.balance = initial_balance
        self.user_name = user_name
        self.get_balance()
    
    def get_balance(self):
        print(f"\nThe user '{self.user_name}' has ${self.balance} left.")

    def Validate_Transition(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, the user '{self.user_name}' only has ${self.balance} left.")

    def deposit(self, amount):
        if amount < 0:
            print("\nThe deposit can't be lower than 0.")
        else:
            self.balance += amount
            print("\nDeposit complete.")
            self.get_balance()

    def withdraw(self, amount):
        try:
            self.Validate_Transition(amount)
            self.balance -= amount
            print("\nWithdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print("\nWithdraw interrupted.")
            print(error)

    def transfer(self, amount, account):
        try:
            print("\n----- Starting transfer. -----")
            self.Validate_Transition(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"\nUser '{self.user_name}' transferred ${amount} to user '{account.user_name}'")
            print("\n----- Transfer complete. -----")
        except BalanceException as error:
            print("\nTranfer interrupted.")
            print(error)

