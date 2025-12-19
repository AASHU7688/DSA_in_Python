# Sorting elements of an array by frequency
n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

# Step 1: Count frequency
freq = {}
for x in arr:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

# Step 2: Store unique elements
unique = []
for x in freq:
    unique.append(x)

# Step 3: Sort unique elements by frequency (desc) and value (asc)
for i in range(len(unique)):
    for j in range(i + 1, len(unique)):
        if freq[unique[i]] < freq[unique[j]] or \
           (freq[unique[i]] == freq[unique[j]] and unique[i] > unique[j]):
            temp = unique[i]
            unique[i] = unique[j]
            unique[j] = temp

# Step 4: Print elements according to frequency
for x in unique:
    for i in range(freq[x]):
        print(x, end=" ")
