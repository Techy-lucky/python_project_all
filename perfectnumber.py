n = int(input("enter the number : "))
new = n
total = 0
fresh = 0
for i in range(1,n+1):
        total +=i
        if total <= n :
                fresh = total 

print(fresh)

if fresh == new:
        print("its a prefect number")
else:
        print("no its not a perfect number ")




