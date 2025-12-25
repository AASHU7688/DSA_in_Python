# Prime numbers in a given range
s=int(input("enter the number from where you want to start: "))
e=int(input("enter the number where you want to end: "))

for n in range(s,e+1):
    if n <= 1:
        continue 
    
    for i in range(2,n):
        if n%i==0:
            break
    else:
        print(n,end=" ")
