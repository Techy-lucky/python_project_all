a = int(input("enter the value of a : "))
b = int(input("enter the value of b : "))

# a = 10 
# b = 20

print(f"before swap a = {a} and b = {b}")

a = a + b 
b = a - b 
a = a - b 

print(f"after swap a = {a} and b = {b}")
