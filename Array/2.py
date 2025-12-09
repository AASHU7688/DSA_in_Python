#Find the smallest number in an array
n=int(input("enter the how many numbers you want in array: "))
arr=[]
for i in range(n):
    x=int(input("enter the values: "))
    arr.append(x)
    
mini=arr[0]

for i in range(1,len(arr)):
    if arr[i]<mini:
        mini=arr[i]
print(mini)