# Adding Element in an array
n=int(input("enter the how many values you want in array: "))
arr=[]
for i in range(n):
    x=int(input("enter the value in array: "))
    arr.append(x)
    
pos=int(input("enter at what position you want to add the element: "))
new_element=int(input("enter the value of new element: "))

arr.append(0)

for i in range(n,pos,-1):
    arr[i]=arr[i-1]
    
arr[pos]=new_element

for x in arr:
    print(x,end=" ")
