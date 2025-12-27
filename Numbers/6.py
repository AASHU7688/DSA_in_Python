#Sum of Prime Numbers in a Given Range
s = int(input("enter start: "))
e = int(input("enter end: "))

total = 0

for n in range(s, e + 1):
    if n <= 1:
        continue

    for i in range(2, n):
        if n % i == 0:
            break
    else:
        total += n

print("Sum of prime numbers:", total)
