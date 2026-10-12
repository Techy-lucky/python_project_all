# create a simple calculator in python 

val1 = int(input("enter the value 1 : "))
val2 = int(input("enter the value 2 : "))
op = input("enter the operand from this + , - , * , / , %  :")

match op:
    case '+':
        sum = val1 + val2
        print(f"The addition of both value is {sum}")
    case '-':
        sum = val1 - val2
        print(f"The subtraction of both value is {sum}")
    case '*':
        sum = val1 * val2
        print(f"The multiplication of both value is {sum}")
    case '/':
        if(val2 == 0):
            print("print value cannot be devided by zero")
        else :
            sum = val1 / val2
            print(f"The division of value is {sum}")
    case '%':
        sum = val1 % val2
        print(f"The remainder of value is {sum}")
    case _:
        print("invalid option")