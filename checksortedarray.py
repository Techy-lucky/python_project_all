arr = []
n = int(input("enter the number for array : "))
for i in range(1,n+1):
    j = int(input("enter the array :"))
    arr.append(j)
print(arr)
data = sorted(arr)
print(data)
if data == arr :
    print("sorted")
else :
    print("not sorted") 
