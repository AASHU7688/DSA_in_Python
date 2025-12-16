#Find all repeating elements in an array
n=int(input("enter the how many values you want in array: "))
arr=[]
for i in range(n):
    x=int(input("enter the value in array: "))
    arr.append(x)
    
freq = {}

for x in arr:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

for key in freq:
    if freq[key] > 1:
        print(key, end=" ")
