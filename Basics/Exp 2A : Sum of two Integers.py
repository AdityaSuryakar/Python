#Write a Python program to sum of two given integers. However, if the sum is
#between 15 to 20, display the result on output console. [Use if.... Statement]

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

total = num1 + num2

if 15 <= total <= 20:
    print(f"The sum is {total}, which is between 15 and 20.")
