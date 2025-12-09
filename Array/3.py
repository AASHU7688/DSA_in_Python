#Find the largest number in an array
n=int(input("enter the how many numbers you want in array: "))
arr=[]
for i in range(n):
    x=int(input("enter the values: "))
    arr.append(x)
    
maxx=arr[0]
for i in range(1,len(arr)):
    if arr[i]>maxx:
        maxx=arr[i]
print(maxx)