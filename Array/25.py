#Search an element in an array 
n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

key = int(input())

found = False

for i in range(n):
    if arr[i] == key:
        print("Element found at index", i)
        found = True
        break

if not found:
    print("Element not found")
