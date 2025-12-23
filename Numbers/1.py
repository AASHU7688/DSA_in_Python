#Check if a number is palindrome or not
n=int(input("enter the number: "))

original = n
rev = 0

digit=len(str(n))

for i in range(digit):
    digit=n%10
    rev=rev*10+digit
    n=n//10
    
if rev == original:
    print("Number is palindrome")
    
else:
    print("Number is not an palindrome")
