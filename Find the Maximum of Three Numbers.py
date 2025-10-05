#15. Find the Maximum of Three Numbers
(Write a function that takes three numbers as input and returns the maximum of the three )

def largest(a,b,c):
    if a>b and a>c:
        print(f" {a} is maximum ")
    elif b>c and b>a:
        print(f" {b} is maximum ")
    else:
        print(f" {c} is maximum ")

num1=int(input(print("Enter first number")))
num2=int(input(print("Enter second number")))
num3=int(input(print("Enter third number")))
largest(num1,num2,num3)
