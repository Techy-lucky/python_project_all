arr = []
count = 0
n = int(input("enter the number for array : "))
for i in range(1,n+1):
    j = int(input("enter the array :"))
    # arr.append(j)
    if int(j)%2!=0:
        count += 1

print(f"total odd value in arr : {count}")