# Check if a number is prime or not 
n=int(input("enter any number: "))

if n<=1:
    print("Not Prime")
    
else:
    count=0
    
for i in range(n,n+1):
    if n%i==0:
        count+=1

if count == 2:
    print("Not Prime")

else:
    print("Prime")
