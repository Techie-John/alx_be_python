class BankAccount:
    """A simple bank account class."""

    def __init__(self, initial_balance=0):
        """Initializes the account with a given balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposits a specified amount into the account."""
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if funds are sufficient.
        Returns True for a successful withdrawal, False otherwise.
        """
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Prints the current account balance."""
        print(f"Current Balance: ${self.account_balance}")