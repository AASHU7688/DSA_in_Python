
# Second Smallest and Second Largest element in an array

n = int(input("enter the size of arr: "))
arr = []

for i in range(n):
    x = int(input("enter the value of array: "))
    arr.append(x)

minn = float('inf')
second_minn = float('inf')
maxx = float('-inf')
second_maxx = float('-inf')

# Find second minimum
for x in arr:
    if x < minn:
        second_minn = minn
        minn = x
    elif x < second_minn and x != minn:
        second_minn = x

print("Second smallest:", second_minn)

# Find second maximum
for x in arr:
    if x > maxx:
        second_maxx = maxx
        maxx = x
    elif x > second_maxx and x != maxx:
        second_maxx = x

print("Second largest:", second_maxx)
