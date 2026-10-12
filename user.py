a = int(input("enter the number for a : "))
b = int(input("enter the number for b : "))
c = int(input("enter the number for c : "))

if(a>b and a>c):
    print("a is greater than b and c")
elif(b>a and b>c):
    print("b is greater than a and c")
else:
    print("c is greater than a and b")