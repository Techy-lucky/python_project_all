# 1 print sum of first 10 even number

# num = int(input("enter the number how many you want to print : "))
# total = 0
# for i in range(0,num+1):
#     # print(i)
#     if(i%2==0):
#         total+= i 

# print(f"sum of even number is : {total}")

# 2 accept two value s and n print square of first n number stating from s 

# S = int(input("enter the value of S : "))
# N = int(input("enter the value of N : "))

# for i in range(S,N+1+S):
#     print(i**2)


# 3 reverse the accpet string

# name = "lakshit"
# print(f"before string : {name}")
# print(f"after reverse string : {name[::-1]}")

# 4 accept sentence from user and count the vowels

# string = input("enter your string : ")
# vowel = "aeiouAEIOU"
# count = 0
# # vowel.split()
# # print(vowel)
# print(string)

# for i in string:
#     if i in vowel:
#         count +=1
# print(count)

# 5 remove duplicate from list

# lists = [22,33,44,55,22,44,56,55,23]
# print(lists)

# for i in range(len(lists)-1,-1,-1):
#     for j in range(i):
#         if lists[i] == lists[j]:
#             lists.pop(i)
#             break
# print(lists)

# 6 reverse the list

# l = [1,2,3,4,5,6,7,8]
# print(f"before list reverse : {l}")
# l.reverse()
# print(f"after list reverse : {l}")

# 7 print * pattern

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
