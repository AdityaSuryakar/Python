#Write a program to perform different Identity Operations on numbers in Python.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

is_result = a is b
is_not_result = a is not b

print("\n--- Identity Operations ---")
print(f"a = {a}, b = {b}")
print(f"a is b → {is_result}")
print(f"a is not b → {is_not_result}")
