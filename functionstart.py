# def greet():
#     print("hello")

# greet()


# def greet(name):
#     print("hello", name)

# greet("lakshit")


# def sum(a,b):
#     print(a + b)

# sum(23,43)  


# def pi():
#     return 3.14

# pi()


# def add(a,b):
#     return a+b

# add(22,44)


# def name(name = "student"):
#     print("hello",name)

# name()


# def add():
#     a = int(input("enter the value of a : "))
#     b = int(input("enter the value of a : "))

#     c = a+b
#     print(f"addition of a and b is : {c}")

# def sub():
#     a = int(input("enter the value of a : "))
#     b = int(input("enter the value of a : "))

#     c = a-b
#     print(f"subtraction of a and b is : {c}")

# def mul():
#     a = int(input("enter the value of a : "))
#     b = int(input("enter the value of a : "))

#     c = a*b
#     print(f"multiplication of a and b is : {c}")

# def dev():
#     a = int(input("enter the value of a : "))
#     b = int(input("enter the value of a : "))

#     c = a/b
#     print(f"devision of a and b is : {c}")

# add()
# sub()
# mul()
# dev()

# recusion

# def num(n):
#     print(n)
#     num(n-1)

# num(10)

# def countdown(n):
#     for i in range(1,n+1):
#         print(1)

# countdown(10)

# def fact(f):
#     a = f*f-1
#     print(a)
# fact(5)

# def square(n):
#     return n*n

# # square = lambda n:n*n
# # print(square)

# square(2)


# square = lambda n:n*n
# print(square(8))

# add =lambda n:n+n
# print(add(4))

def fun(n):
    if n==0:
        return
    fun(n-1)
    print(n)

fun(3)