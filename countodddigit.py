n = int(input("enter the value : "))
count = 0
data = str(n)
total = 0
for i in data :
    if int(i)%2!=0 :
        count += 1
        total = count
print(f"total odd value : {total}")