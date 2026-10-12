# write a program to check if a person is eligable for discount the criteria is he must be a student and age is must be below 1
# input values to take are role and age
# example : eligable : true
# role must be either student or teacher 


role = input("enter your role :")
age = int(input("enter the age : "))
dscount = bool(role.lower()== "student" and age<=21)
print(f"eligable : {dscount}")