#Find all Palindrome numbers in a given range
L = int(input("Enter starting range: "))
R = int(input("Enter ending range: "))

for num in range(L, R + 1):
    original = num
    temp = num
    rev = 0

    digits = len(str(num))

    for i in range(digits):
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10

    if rev == original:
        print(original, end=" ")
