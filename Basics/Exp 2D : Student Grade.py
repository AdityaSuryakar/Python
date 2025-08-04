# Write a Python program to accept marks of three subjects in the range of 0 to 100.If the marks in all
# three subjects are greater than 40 then calculate the percentage.Assign the appropriate grade as per following
# a. For percentage greater than or equal to 75, assign “Outstanding”.
# b. For percentage is greater than or equal to 70 to less than 75, assign “Distinction Grade”.
# c. For percentage is greater than or equal to 60 to lessthan 70, assign “A Grade”.
# d. For percentage is greater than or equal to 50 to less than 60, assign “B Grade”.
# e. For percentage is greater than or equal to 40 to lessthan 50, assign “C Grade”.
# f. For marks in any of the subject are less than 40, assign “Fail Grade”.
# Print out an appropriate assign grade message to the user. [Use if... elif....else statement]
sub1 = int(input("Enter marks for Subject 1 (0-100): "))
sub2 = int(input("Enter marks for Subject 2 (0-100): "))
sub3 = int(input("Enter marks for Subject 3 (0-100): "))
if 0 <= sub1 <= 100 and 0 <= sub2 <= 100 and 0 <= sub3 <= 100:
    if sub1 >= 40 and sub2 >= 40 and sub3 >= 40:
        total = sub1 + sub2 + sub3
        percentage = total / 3
        if percentage >= 75:
            grade = "Outstanding"
        elif 70 <= percentage < 75:
            grade = "Distinction Grade"
        elif 60 <= percentage < 70:
            grade = "A Grade"
        elif 50 <= percentage < 60:
            grade = "B Grade"
        elif 40 <= percentage < 50:
            grade = "C Grade"
        print(f"\nPercentage: {percentage:.2f}%")
        print(f"Grade: {grade}")
    else:
        print("\nGrade: Fail Grade ")
else:
    print("\nInvalid input! Marks must be between 0 and 100.")
