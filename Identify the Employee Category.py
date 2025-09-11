#1. Identify the Employee Category 
#A company categorizes its employees based on their salaries: 
#Salary above ₹50,000 → "High Income" 
#Salary between ₹30,000 and ₹50,000 → "Medium Income" 
#Salary below ₹30,000 → "Low Income" 
#Write a Python program that takes an employee’s salary as input and prints their category. 
income = int(input("Enter the income"))
if(income < 30000):
    print("Low Income")
elif(income > 50000):
    print("High Income")
elif(income > 30000 and income < 50000):
    print("Medium Income")
