#Count frequency of each element in an array
n=int(input("enter the space of array: "))
arr=[]
for i in range(n):
    x=int(input("enter the value of an array: "))
    arr.append(x)

freq={}

for x in arr:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1
        
for key in freq:
    print(key,freq[key])
