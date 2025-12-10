#Find the second smallest number in an array
n=int(input("enter the how many numbers you want in array: "))
arr=[]
for i in range(n):
    x=int(input("enter the values: "))
    arr.append(x)
    
minn=float('inf')
second_minn=float('inf')

for x in arr:
    if x<minn:
        second_minn=minn
        minn=x
        
    elif x<second_minn and x!=minn:
        second_minn=x
        
print(second_minn)

