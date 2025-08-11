#Exp 3C - Prime Number
#PRN : 23UAM132 

num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is NOT a Prime number.")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a Prime number.")
    else:
        print(f"{num} is NOT a Prime number.")
