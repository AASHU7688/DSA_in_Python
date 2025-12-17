#Find all symmetric pairs in array 
n = int(input("enter how many values you want in array: "))
pairs = []

for i in range(n):
    a, b = map(int, input().split())
    pairs.append((a, b))

mp = {}

for a, b in pairs:
    if b in mp and mp[b] == a:
        print(b, a)
    else:
        mp[a] = b
