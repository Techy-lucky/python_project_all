# create a list of 10 numbers print the sum of last four elements of the list
# find out the different betwern max and min elemnt of the list 
# insert a number in a list at 6 postion this number must be 1/3 of number stored at 4 position


list1 = [10,20,45,35,32,65,12,56,32,21]

# print(len(list))

# 1
# print(list[6])

new = list1[-1:-5:-1]
print(new)
print(sum(new))

# new1 = [1,2,3,4,5]
# print(new1[-1:-6:-1])

# 2 
l = max(list1)
print(l)

m = min(list1)
print(m)

print(l-m)

# 3
l1 = list1[4] ## fouth position
print(l1)

result = round(l1*1/3,2)
# print(result)
new_l1 = list1
# print(new_l1)
new_l1.insert(6,result)
print(new_l1)


# 4
name = "lakshit varma xz"

n = max(name)
print(n)


# 
