#Write a program to check num is armstrong or not.
num = int(input("Enter a number: "))
power = len(str(num))
total = 0
for digit in str(num):
    total += int(digit) ** power

if total == num:
    print(num,"is an Armstrong number.")
else:
    print(num,"is NOT an Armstrong number.")
