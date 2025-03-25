#3. Imagine you are designing a basic ATM-like interface where users can:balance = 0

print("MENU=>\n1. Check Balance\n2. Deposit\n3. Withdraw Money\n4. Exit the System")

while True:
   
        choice = int(input("Enter your choice: "))
        if choice == 1:  # Check balance
            print(f"Balance is: {balance}")
        elif choice == 2:  # Deposit money
            money = int(input("Deposit the amount: "))
            balance += money
            print(f"You deposited {money}. New balance: {balance}")
        elif choice == 3:  # Withdraw money
            money = int(input("Withdraw the amount: "))
            if money <= balance:
                balance -= money
                print(f"You withdrew {money}. Remaining balance: {balance}")
            else:
                print("Insufficient balance!")
        elif choice == 4:  # Exit the system
            print("Exiting the system. Thank you!")
            break
        
        else:
            print("Invalid choice. Please try again.")  
        
   
