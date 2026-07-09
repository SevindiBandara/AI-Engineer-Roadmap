class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        else:
            return "Deposit amount must be positive."
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."
    def check_balance(self):
        return f"Current balance: ${self.__balance}"
    
# Example usage
account = BankAccount("John Doe", 1000) 
print(account.check_balance())  # Accessing the balance through a public method
print(account.deposit(500))     # Depositing money
print(account.withdraw(200))    # Withdrawing money
print(account.check_balance())  # Checking balance after transactions