#Check if a number is palindrome or not
n=int(input("enter the number: "))

original = n
rev = 0
digits=len(str(n))

for i in range(digits):
    digits=n%10
    rev = rev * 10 + digits
    n=n//10
    
if rev == original:
    print("Number is palindrome")

else:
    print("Number is not palindrome")
