num1 = int(input("Enter a number to check: "))

if num1 <= 1:
    print(f"{num1} is not a prime number.")
else:
    for i in range(2, num1):
        if num1 % i == 0:
            print(f"{num1} is not a prime number.")
            break
    else:
        print(f"{num1} is a prime number.")