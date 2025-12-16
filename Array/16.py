# Remove duplicates from an unsorted array
n=int(input("enter the how many values you want in array: "))
arr=[]
for i in range(n):
    x=int(input("enter the value in array: "))
    arr.append(x)
    
unique=[]

for i in range(n):
    if arr[i] not in unique:
        unique.append(arr[i])
    
for x in unique:
    print(x,end=" ")
