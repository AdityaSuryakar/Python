# ATM Withdrawal System

# Initialize account balance
balance = 1000  # Example starting balance

# Get withdrawal amount from user
amount = int(input("Enter the amount to withdraw: "))

# Check if the withdrawal amount is a multiple of 10
if amount % 10 != 0:
    print("Error: Amount must be a multiple of 10.")
else:
    # Check if the user has enough balance
    if amount <= balance:
        balance -= amount
        print(f"Withdrawal successful! Your new balance is: ${balance}")
    else:
        print("Error: Insufficient funds.")
