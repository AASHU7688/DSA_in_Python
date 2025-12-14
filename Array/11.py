# Rearrange array in increasing-decreasing order
n = int(input("enter how many value you want in array: "))
arr = []

for i in range(n):
    x = int(input("enter the value of an array: "))
    arr.append(x)

# Step 1: Sort array in increasing order
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

for x in arr:
    print(x, end=" ")
print()

# Step 2: Rearrange second half in decreasing order
mid = n // 2

for i in range(mid, n):
    for j in range(i + 1, n):
        if arr[i] < arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

for x in arr:
    print(x, end=" ")
