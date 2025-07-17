#Check the number is palindrome.
num = int(input("Enter the number :"));
original = num;
reverse = 0;
digits =len(str(num));
for i in range (digits):
    digits = num%10;
    reverse = reverse * 10 + digits;
    num = num // 10;
if original == reverse:
    print(original,"Palindrome");
else:
    print(original,"Not Palindrome");
