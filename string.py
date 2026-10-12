# upper is use to change the upper case of a string

print()
greeting = "hello lakshit!"
print(f"before greeting : {greeting}")
greeting.upper()
print(f"after greeting : {greeting.upper()}")
print()

# lower is use to change the lower case of a string

signal = "GREEN"
print(f"before signal : {signal}")
print(f"after signal : {signal.lower()}")
print()

# replace is use to swap all occurrences of a speified witrh a new string
text = "hello i am lakshit and i like dogs and dogs are very cute"
print(f"before text : {text}")
print(f"after text : {text.replace("dogs","cats")}")
print()

# split is use to split the string into some list 
number = "1 2 3 4 5"
print(f"before split : {number}")
list_no = number.split()
print(f"after split : {list_no}")
print()

# strip remove white space from the string
space = "    hello lakshit!     "
print(f"before space : {space}")
print(f"after space : {space.strip()}")