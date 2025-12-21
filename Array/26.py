#Sort an array according to the order defined by another array 
n = int(input())
arr1 = []

for i in range(n):
    arr1.append(int(input()))

m = int(input())
arr2 = []

for i in range(m):
    arr2.append(int(input()))

# Step 1: Count frequency of arr1
freq = {}

for x in arr1:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

# Step 2: Print elements as per arr2 order
result = []

for x in arr2:
    if x in freq:
        for i in range(freq[x]):
            result.append(x)
        del freq[x]

# Step 3: Remaining elements (sort manually)
remaining = []

for x in freq:
    for i in range(freq[x]):
        remaining.append(x)

# Manual sort (Bubble sort)
for i in range(len(remaining)):
    for j in range(i + 1, len(remaining)):
        if remaining[i] > remaining[j]:
            temp = remaining[i]
            remaining[i] = remaining[j]
            remaining[j] = temp

# Step 4: Combine result
for x in remaining:
    result.append(x)

# Output
for x in result:
    print(x, end=" ")
