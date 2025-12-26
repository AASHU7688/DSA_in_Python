#count prime number in range
s = int(input("enter start: "))
e = int(input("enter end: "))

count = 0

for n in range(s, e + 1):
    if n <= 1:
        continue

    for i in range(2, n):
        if n % i == 0:
            break
    else:
        count += 1

print("Total prime numbers:", count)
