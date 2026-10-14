arr = []
total = 0
n = int(input("enter the number for array : "))
for i in range(1,n+1):
    j = int(input("enter the array :"))
    arr.append(j)
    total += j
print(arr)
print(total)