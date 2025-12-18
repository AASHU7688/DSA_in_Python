#Replace each element of the array by its rank in the array
n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

# Step 1: Copy array
temp = arr[:]

# Step 2: Sort temp array (Bubble Sort)
for i in range(n):
    for j in range(i + 1, n):
        if temp[i] > temp[j]:
            temp[i], temp[j] = temp[j], temp[i]

# Step 3: Assign ranks
rank = {}
r = 1

for i in range(n):
    if temp[i] not in rank:
        rank[temp[i]] = r
        r += 1

# Step 4: Replace elements with ranks
for i in range(n):
    arr[i] = rank[arr[i]]

# Output
for x in arr:
    print(x, end=" ")
