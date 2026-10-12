num = int(input("please enter the positive grp of number : "))
count = 0
if num==0:
    print(1)
else:
    while num>0:
        count = count +1
        num//=10
    print(count)