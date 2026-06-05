# Custom Exception
class InsufficientFundsError(Exception):
    pass


# Parent Class
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.balance += amount
        self.transactions.append(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Insufficient funds! Available balance: ₹{self.balance}"
            )

        self.balance -= amount
        self.transactions.append(f"Withdrawn ₹{amount}")

    def get_balance(self):
        return self.balance

    def transaction_history(self):
        return self.transactions

    def __str__(self):
        return f"Account Owner: {self.owner}, Balance: ₹{self.balance}"


# Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest

        self.transactions.append(
            f"Interest Added ₹{interest:.2f}"
        )


# Current Account
class CurrentAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit=0):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance - amount < -self.overdraft_limit:
            raise InsufficientFundsError(
                f"Overdraft limit exceeded! Limit: ₹{self.overdraft_limit}"
            )

        self.balance -= amount
        self.transactions.append(f"Withdrawn ₹{amount}")