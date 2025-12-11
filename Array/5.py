#Find the second largest number in an array
n=int(input("enter the how many numbers you want in array: "))
arr=[]
for i in range(n):
    x=int(input("enter the values: "))
    arr.append(x)
    
maxx = float('-inf')
max_second = float('-inf')

for x in arr:
    if x > maxx:
        max_second=maxx
        maxx=x
    elif  x > max_second and x != max_second:
        max_second=x
        
print(max_second)