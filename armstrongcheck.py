n = int(input("enter the value : "))
num = n
count = 0
store = 0
total = 0
for i in str(n):
    count += 1
print(count)
for j in str(n):
    store = int(j)**count
    total += store
print(total)