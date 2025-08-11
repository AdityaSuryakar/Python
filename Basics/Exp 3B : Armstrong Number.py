#Exp 3B - Armstrong Number

num = int(input("Enter a number: "))
original_num = num
sum_of_powers = 0
digits = len(str(num))
while num > 0:
    digit = num % 10               
    sum_of_powers += digit ** digits 
    num //= 10                     
if original_num == sum_of_powers:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is NOT an Armstrong number.")
