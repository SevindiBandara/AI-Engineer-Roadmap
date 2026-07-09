class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
        
    def show_balance(self):
        return f"Current balance: ${self.__balance}"
    
account = BankAccount(1000)
print(account.show_balance())  # Accessing the balance through a public method

