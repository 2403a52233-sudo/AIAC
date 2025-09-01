class BankAccount:
    def __init__(self, name, balance=0): 
        self.name = name
        self.balance = balance
    def deposit(self, amt): 
        if amt > 0:
            self.balance = self.balance + amt
            return f"Deposited {amt}. Balance: {self.balance}"
        else:
            return "Deposit must be positive."
    def withdraw(self, amt): 
        if amt > 0:
            if amt <= self.balance:
                self.balance = self.balance - amt
                return f"Withdrew {amt}. Balance: {self.balance}"
            else:
                return "Insufficient funds."
        else:
            return "Withdrawal must be positive."
    def get_balance(self): 
        return f"Balance: {self.balance}"
if __name__ == "__main__":
    acc = BankAccount(input("Name: "), float(input("Initial balance: ")))
    while True:
        c = input("\n1.Deposit 2.Withdraw 3.Balance 4.Exit\nChoose: ")
        if c == "1": print(acc.deposit(float(input("Deposit amount: "))))
        elif c == "2": print(acc.withdraw(float(input("Withdraw amount: "))))
        elif c == "3": print(acc.get_balance())
        elif c == "4": break
        else: print("Invalid choice.")