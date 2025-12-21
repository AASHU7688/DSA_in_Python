# Check if Array is a subset of another array or not
n = int(input())
arr1 = []

for i in range(n):
    arr1.append(int(input()))

m = int(input())
arr2 = []

for i in range(m):
    arr2.append(int(input()))

# Count frequency of arr1
freq = {}

for x in arr1:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

# Check subset
is_subset = True

for x in arr2:
    if x not in freq or freq[x] == 0:
        is_subset = False
        break
    freq[x] -= 1

if is_subset:
    print("YES")
else:
    print("NO")
