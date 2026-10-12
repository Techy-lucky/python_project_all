age = int(input("please enter the age : "))
has_id = bool(input("please say True or False for id :"))

if(age>=18):
    if has_id == True :
        print("entery allowed")
    else :
        print("entery not allowed")
else :
    print("you are in under age ")