# Find the median of the given array
n=int(input("enter how many values you want in array: "))
arr=[]
for i in range(n):
    x=int(input("enter the values of an array: "))
    arr.append(x)
    
for i in range(n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp

if n%2!=0:
    median=arr[n//2]
else:
    median=(arr[n//2 -1]+arr[n//2])/2
    
print(median)
