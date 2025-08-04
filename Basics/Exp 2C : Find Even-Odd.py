# Write a Python program to find whether a given number  is
# even or odd, print out an appropriate message to the user. 
# [ use ternary operator]
num = int(input("Enter a number: "))
result = "Even" if num % 2 == 0 else "Odd"

print(f"The number {num} is {result}.")
