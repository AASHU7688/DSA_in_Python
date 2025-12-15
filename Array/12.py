#Calculate sum of the elements of the array
n=int(input("enter the how many value you want in array: "))
arr=[]
for i in range(n):
    x=int(input("enter the value of array: "))
    arr.append(x)
sum=0   
for i in range(n):
    sum += arr[i]
    
print(sum)
    
