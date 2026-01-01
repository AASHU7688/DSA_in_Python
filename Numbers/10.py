# strong number 

n = int(input("enter number: "))

temp = n
total = 0

while temp > 0:
    digit = temp % 10
    fact = 1

    for i in range(1, digit + 1):
        fact *= i

    total += fact
    temp //= 10

if total == n:
    print("Strong number")
else:
    print("Not Strong number")