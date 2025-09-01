class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. Balance: {self.balance}")
        else:
            print("Invalid amount")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount")
    def check_balance(self):
        print(f"Balance: {self.balance}")
        return self.balance
name = input("Enter name: ")
balance = float(input("Enter initial balance: "))
account = BankAccount(name, balance)
while True:
    choice = input("1.Deposit 2.Withdraw 3.Balance 4.Exit: ")
    if choice == "1":
        amount = float(input("Amount: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Amount: "))
        account.withdraw(amount)
    elif choice == "3":
        account.check_balance()
    elif choice == "4":
        break
