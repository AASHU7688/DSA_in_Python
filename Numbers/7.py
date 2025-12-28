#Largest & Smallest Prime Number in a Given Range
s = int(input("enter start: "))
e = int(input("enter end: "))

smallest = None
largest = None

for n in range(s, e + 1):
    if n <= 1:
        continue

    for i in range(2, n):
        if n % i == 0:
            break
    else:
        if smallest is None:
            smallest = n
        largest = n

if smallest is None:
    print("No prime numbers in the range")
else:
    print("Smallest prime:", smallest)
    print("Largest prime:", largest)
