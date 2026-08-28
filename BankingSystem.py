# Its a banking system project with OOP concepts

class Account:
    def __init__(self, account_holder, initial_balance=0):
        self.__account_holder = account_holder
        self.__balance = initial_balance 
        self.__account_number = id(self) 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew {amount}. New balance: {self.__balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.__balance

class SavingsAccount(Account):
    def __init__(self, account_holder, initial_balance=0):
        super().__init__(account_holder, initial_balance)
        self.interest_rate=self.interest_rate