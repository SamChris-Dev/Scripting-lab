class InsufficientFundsError(Exception): 
    """Raised when a bank account withdrawal attempt exceeds available funds."""
    pass


class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Not enough funds in your account!")
        self.balance -= amount



try:
    account = Account(100)
    account.withdraw(150)  
except InsufficientFundsError as e:
    print(e)  # Output: Not enough funds in your account!
