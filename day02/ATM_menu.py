balance = 1000
while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        print(f"Your current balance is: ${balance}")
    elif choice == '2':
        deposit_amount = float(input("Enter the amount to deposit: "))
        balance += deposit_amount
        print(f"${deposit_amount} deposited successfully.")
    elif choice == '3':
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        if withdraw_amount <= balance:
            balance -= withdraw_amount
            print(f"${withdraw_amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")