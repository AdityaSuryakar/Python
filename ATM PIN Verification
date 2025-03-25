# 5. #ATM PIN Verification 
(A bank ATM allows a user to enter their PIN a maximum of 3 times. If the correct PIN (1234) is 
entered within 3 attempts, the user gains access; otherwise, the card is blocked. Write a Python 
program for this. )

correct_pin = 1234
count=0
for i in range(1,4):
    pin = int(input(f"Enter the pin at {i}th attempt"))
    if pin == correct_pin:
        print("gains access")
    elif pin != correct_pin:
        print("Wrong Pin")
        count += 1
    
if count==3:      
        print("Maximum attempts.Card is blocked")
        
        
