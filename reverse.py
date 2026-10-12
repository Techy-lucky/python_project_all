num = int(input("please enter the number : "))
rev=0
rem=0
num1= num

while num>0:
    rem = num%10
    rev=(rev*10)+rem
    num=num//10
print(rev)

if num1 == rev:
        print(bool(True))
else:
      print(bool(False))