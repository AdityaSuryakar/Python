#Write a program to perform different Membership Operations on numbers in Python.

number_list = [10,20,30,40,50]
num = int(input("Enter a number to check membership: "))

in_result = num in number_list
not_in_result = num not in number_list

print("\n--- Membership Operations ---")
print(f"{num} in {number_list} → {in_result}")
print(f"{num} not in {number_list} → {not_in_result}")
