#Check number is prime
num = int(input("Enter the number: "))

# Initialize isPrime as True
isPrime = True

if num <= 1:
    isPrime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            isPrime = False
            break

if isPrime:
    print(num,"is Prime Number")
else:
    print(num,"is Not Prime Number")
