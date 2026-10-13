# write a program to read a file and count how many vowels are present in its content 
# read all lines from a file into a list . print the total number of lines and display the 2nd and 4th line 
# take a sentence from the user ,split it into words ,and store them in a list print the longest word 
# read a file ,split its content into words and store them in a list (1) prints the total number of words (2) print all unique words 

# 1
count = 0
with open(r"/home/lakshit/Python_repo_all/fileoperation/demo1.txt","r") as f :
    content = f.read()
    for i in content :
        if i.lower() in "aeiou":
            count += 1
    print(f"total vowels are : {count}") 
    print()
    print()


# 2
with open(r"/home/lakshit/Python_repo_all/fileoperation/demo1.txt","r") as f :
    content = f.readlines()
    print(f"Total numbers of line are in a list : {len(content)}")
    print()
    print(f"2nd line in a list : {content[1]}")
    print(f"4th line in a list : {content[3]}")
    print()
    print()

# 3
user = input("enter the sentence : ")
spt = user.split()
longest = ""
print(spt)
for i in spt:
    if len(i) > len(longest):
        longest = i 
print(f"longest word in the list : {longest}")


# 4
with open(r"/home/lakshit/Python_repo_all/fileoperation/demo1.txt","r") as f :
    content = f.read()
    words_list = content.split()
    print("Total number of words:", len(words_list))
    unique_words = list(set(words_list))
    print("Unique words:", unique_words)
