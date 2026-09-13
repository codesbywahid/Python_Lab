class Account():
    def __init__(self, acc_num, name, initial_balance):
        self.acc_num = acc_num
        self.name = name
        self.initial_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.initial_balance += amount
            print("Amount deposited is ", amount, ". New balance is : ", self.initial_balance)
        else:
            print("Amount not deposited")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.initial_balance:
                self.initial_balance -= amount
                print("Amount deducted is ", amount, ". Remaining balance is : ", self.initial_balance)
            else:
                print("Insufficient balance")
        else:
            print("Invalid withdrawal amount")

    def balance(self):
        return self.initial_balance


class Savings(Account):
    def __init__(self, acc_num, name, initial_balance, interest_rate):
        super().__init__(acc_num, name, initial_balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.initial_balance * (self.interest_rate / 100)
        self.initial_balance += interest
        print("Interest added. New balance is : ", self.initial_balance)


class Current_Account(Account):
    def __init__(self, acc_num, name, initial_balance, Overdrawn_limit):
        super().__init__(acc_num, name, initial_balance)
        self.Overdrawn_limit = Overdrawn_limit

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.initial_balance + self.Overdrawn_limit:
                self.initial_balance -= amount
                print("Amount deducted. Remaining balance is : ", self.initial_balance)
            else:
                print("Exceeds overdraft limit")
        else:
            print("Invalid withdrawal amount")


class Bank():
    def __init__(self):
        self.accounts = []

    def add_acount(self, acc):
        self.accounts.append(acc)

    def find_account(self, acc_num):
        for acc in self.accounts:
            if acc_num == acc.acc_num:
                return acc
        return None

    def total_deposits(self):
        sum = 0
        for acc in self.accounts:
            sum += acc.balance()
        return sum


bank1 = Bank()

while True:
    print("1.Create Account"
          "\n2.Deposit Money"
          "\n3.Withdraw Money"
          "\n4.Check Balance"
          "\n5.Total Deposits"
          "\n6.Exit")
    choice = input("Enter your choice : ")

    if choice == "1":
        acc_num = input("Enter account number: ")
        name = input("Enter name: ")
        initial_balance = float(input("Enter initial balance: "))
        acc_type = input("Enter account type (normal/savings/current): ").lower()

        if acc_type == "savings":
            interest_rate = float(input("Enter interest rate: "))
            new_acc = Savings(acc_num, name, initial_balance, interest_rate)
        elif acc_type == "current":
            overdraft = float(input("Enter overdraft limit: "))
            new_acc = Current_Account(acc_num, name, initial_balance, overdraft)
        else:
            new_acc = Account(acc_num, name, initial_balance)

        bank1.add_acount(new_acc)
        print("Account created successfully.")

    elif choice == "2":
        acc_num = input("Enter account number: ")
        acc = bank1.find_account(acc_num)
        if acc is None:
            print("Account not found.")
        else:
            amount = float(input("Enter amount to deposit: "))
            acc.deposit(amount)

    elif choice == "3":
        acc_num = input("Enter account number: ")
        acc = bank1.find_account(acc_num)
        if acc is None:
            print("Account not found.")
        else:
            amount = float(input("Enter amount to withdraw: "))
            acc.withdraw(amount)

    elif choice == "4":
        acc_num = input("Enter account number: ")
        acc = bank1.find_account(acc_num)
        if acc is None:
            print("Account not found.")
        else:
            print("Balance: ", acc.balance())

    elif choice == "5":
        print("Total deposits in bank: ", bank1.total_deposits())

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice")