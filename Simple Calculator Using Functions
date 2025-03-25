#14. Simple Calculator Using Functions 
(Write a calculator function that takes two numbers and an operator (+, -, , /) and returns the 
result.) 

def calculator():
    print("MENU=>\n1. Addition (+)\n2. Subtraction (-)\n3. Multiplication (*)\n4. Division (/)\n5. Exit")

    while True:
        first = int(input("Enter the first number: "))
        choice = int(input("Enter your choice: "))

        if choice == 1:
            second = int(input("Enter the second number: "))
            add = first + second
            print(f"Addition result: {add}")
        elif choice == 2:
            second = int(input("Enter the second number: "))
            sub = first - second
            print(f"Subtraction result: {sub}")
        elif choice == 3:
            second = int(input("Enter the second number: "))
            mul = first * second
            print(f"Multiplication result: {mul}")
        elif choice == 4:
            second = int(input("Enter the second number: "))
            if second != 0:
                div = first / second
                print(f"Division result: {div}")
            else:
                print("Error: Division by zero is not allowed.")
        elif choice == 5:
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")
