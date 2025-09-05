#7. ATM Cash Dispensing Machine
(An ATM machine dispenses only ₹500 and ₹2000 notes. Write a Python program that takes an 
amount as input and prints how many ₹2000 and ₹500 notes will be given, assuming the 
amount is a multiple of 500. )
amount = 0
notes = 0
count = 0

amount = int(input("Enter the amount: "))

if amount % 500 == 0:  
    if amount < 2000:
        notes = amount // 500 
        print(f"The 500 notes are: {notes}")
    else:
        notes = amount // 2000
        print(f"The 2000 notes are: {notes}")
        
        remaining_amount = amount % 2000 
        notes = remaining_amount // 500 
        print(f"The 500 notes are: {notes}")
else:
    print("Amount should be in multiples of 500.")
