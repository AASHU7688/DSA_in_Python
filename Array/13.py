#Average of all elements in an array
n=int(input("enter how many values you want in array: "))
arr=[]
for i in range(n):
    x=int(input("enter the values of an array: "))
    arr.append(x)
    
sum=0
avg=0.0

for i in range(n):
    sum+=arr[i]
    avg=sum/n

print(avg)
