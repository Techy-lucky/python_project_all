print("hello")
n = 5
print(f"n = {n}")
conv = str(n)
print(f"str = {conv}")
constr = list(conv)
print(f"list = {constr}")
count = 0

for i in constr:
    # print(i)
    if int(i)%2!=0:
        count += 1
print(count)