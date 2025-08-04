#Write a Python program to accept two integer numbers from user. Find the largest
# number from two integer values and display the result on output console.[Use
# if...else statement]
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

if num1 > num2:
    print(f"The largest number is: {num1}")
else:
    print(f"The largest number is: {num2}")
