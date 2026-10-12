# write a program to convert minute into hours 
# example 135 is 2 hours 15 minute 


minute = int(input("enter the minutes : "))
a = 60
d = minute // a
e = minute % a
# print(f"{d} hours")
# print(f"{e} minute")
print(f"{minute} is {d} hours {e} minutes")