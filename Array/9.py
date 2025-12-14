#array in increasing order
n=int(input("enter the how many values you want in array: "))
arr=[ ]
for i in range(n):
    x=int(input("enter the value of array: "))
    arr.append(x)
    
for i in range(n):
    for j in range(i+1,n):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i]=arr[j]
            arr[j]=temp
for x in arr:
    print(x, end=" ")
