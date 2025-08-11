#Exp 3C - Pattern

# Pattern 1
print("Pattern 1:")
for i in range(1, 5):
    print("*" * i)
print()

# Pattern 2
print("Pattern 2:")
for i in range(1, 5):
    spaces = ' ' * (5 - i)
    stars = '*' * i
    print(spaces + stars)
print()

# Pattern 3
print("Pattern 3:")
for i in range(4, 0, -1):
    print("*" * i)
print()

# Pattern 4
print("Pattern 4:")
for i in range(1, 5):
    print(str(i) * i)
print()

# Pattern 5
print("Pattern 5:")
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()
print()

# Pattern 6
print("Pattern 6:")
rows = 4
for i in range(1, rows + 1):
    # Print leading spaces
    print(' ' * (rows - i) + '* ' * i)
print()

# Pattern 7
print("Pattern 7:")
rows = 4
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))


