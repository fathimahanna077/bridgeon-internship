# Parent Class
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def speak(self):
        print(f"{self.name} says {self.sound}")
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")
    def speak(self):
        print(f"{self.name} says Woof")
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")
    def speak(self):
        print(f"{self.name} says Meow")
dog1 = Dog("Buddy")
cat1 = Cat("Kitty")
dog1.speak()
cat1.speak()





class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary
    def get_info(self):
        return f"Name: {self.name}, Department: {self.department}, Salary: {self.salary}"
    def __str__(self):
        return f"Employee({self.name}, {self.department}, {self.salary})"
emp = Employee("John", "IT", 50000)
print(emp.get_info())
print(emp)







class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0  # Starts at 0
    def drive(self, km):
        self.odometer += km
    def get_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Odometer: {self.odometer} km")
car1 = Car("Toyota", "Corolla", 2022)
car1.drive(100)
car1.drive(50)
car1.get_info()













# Custom Exception
class InsufficientFundsError(Exception):
    pass
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []
    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Deposited ₹{amount}")
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(f"Cannot withdraw ₹{amount}. Insufficient balance.")
        self.balance -= amount
        self.history.append(f"Withdrawn ₹{amount}")
    def get_balance(self):
        return self.balance
    def transaction_history(self):
        return self.history
    def __str__(self):
        return f"Account Holder: {self.owner}, Balance: ₹{self.balance}"
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        self.history.append(f"Interest Added ₹{interest:.2f}")
class CurrentAccount(BankAccount):
    def __init__(self, owner, balance, overdraft_limit):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit
    def withdraw(self, amount):
        if self.balance - amount < -self.overdraft_limit:
            raise InsufficientFundsError(f"Overdraft limit exceeded! Limit = ₹{self.overdraft_limit}")
        self.balance -= amount
        self.history.append(f"Withdrawn ₹{amount}")
print("=== Bank Account ===")
acc = BankAccount("Hanna", 5000)
acc.deposit(2000)
acc.withdraw(1000)
print(acc)
print("Balance:", acc.get_balance())
print("History:", acc.transaction_history())
try:
    acc.withdraw(10000)
except InsufficientFundsError as e:
    print("Error:", e)
print("\n=== Savings Account ===")
save_acc = SavingsAccount("John", 10000, 5)
print("Before Interest:", save_acc)
save_acc.apply_interest()
print("After Interest:", save_acc)
print("History:", save_acc.transaction_history())
print("\n=== Current Account ===")
curr_acc = CurrentAccount("Alice", 5000, 3000)
print("Before Withdrawal:", curr_acc)
curr_acc.withdraw(7000)
print("After Withdrawal:", curr_acc)
try:
    curr_acc.withdraw(2000)
except InsufficientFundsError as e:
    print("Error:", e)
print("History:", curr_acc.transaction_history())

