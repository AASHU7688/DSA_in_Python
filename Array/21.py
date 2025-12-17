# Maximum product subarray in an array
n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

max_ending = arr[0]
min_ending = arr[0]
max_product = arr[0]

for i in range(1, n):
    if arr[i] < 0:
        max_ending, min_ending = min_ending, max_ending

    max_ending = max(arr[i], max_ending * arr[i])
    min_ending = min(arr[i], min_ending * arr[i])

    if max_ending > max_product:
        max_product = max_ending

print(max_product)
