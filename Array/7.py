#Reverse a given array
n=int(input("enter the space of array: "))
arr=[]
for i in range(n):
    x=int(input("enter the value of an array: "))
    arr.append(x)
    
for i in range(n//2):
    temp=arr[i]
    arr[i]=arr[n-i-1]
    arr[n-i-1]=temp

for x in arr:
    print(x,end=' ')
