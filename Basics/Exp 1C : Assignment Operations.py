#Write a program to perform different Assignment Operations on numbers in Python.

num = int(input("Enter a number: "))
print("\n--- Assignment Operations ---")
a = num                             # = operator
print(f"a = {num} -> a = {a}")
a += 5                              # += operator
print(f"a += 5 -> a = {a}")
a -= 2                              # -= operator
print(f"a -= 2 -> a = {a}")
a *= 3                              # *= operator
print(f"a *= 3 -> a = {a}")
a /= 4                              # /= operator
print(f"a /= 4 -> a = {a}")
a %= 3                              # %= operator
print(f"a %= 3 -> a = {a}")
a = num  
a //= 2                             # //= operator
print(f"a //= 2 -> a = {a}")
a **= 2                             # **= operator
print(f"a **= 2 -> a = {a}")
