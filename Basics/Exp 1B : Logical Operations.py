#Write a program to perform different Logical Operations on numbers in Python.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
bool1 = bool(num1)
bool2 = bool(num2)

# Logical operations
logical_and = bool1 and bool2
logical_or = bool1 or bool2
logical_not1 = not bool1
logical_not2 = not bool2

# Output
print("\n--- Logical Operations Results ---")
print(f"{num1} && {num2} = {logical_and}")   # and
print(f"{num1} || {num2} = {logical_or}")     # or
print(f"!{num1} = {logical_not1}")           # not
print(f"!{num2} = {logical_not2}")
