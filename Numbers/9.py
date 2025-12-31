#Check if a number is perfect number

n = int(input("enter number: "))

total = 0

for i in range(1, n):
    if n % i == 0:
        total += i

if total == n and n != 0:
    print("Perfect number")
else:
    print("Not Perfect number")
