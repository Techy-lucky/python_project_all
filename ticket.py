age = int(input("enter the age : "))
ticket = 1000

if(age<=12):
    discount = ticket*10/100
    discount= ticket - discount
    print(f"discounted amount is {discount}")
else :
    print("no discount for you ")