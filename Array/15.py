# Remove duplicates from a sorted array
n=int(input("enter the how many values you want in array: "))
arr=[]
for i in range(n):
    x=int(input("enter the value in array: "))
    arr.append(x)
    
if n==0:
    print("array is empty")
    
else:
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
   
    j=0
    
    for i in range(1,n):
        if arr[i] != arr[j]:
            j+=1
            arr[j]=arr[i]
            
    
    for i in range(j+1):
        print(arr[i],end=" ")
