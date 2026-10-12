# append is use to add element at the end of  the list

fruits = ["apple","banana"]
print("before : ",fruits)
fruits.append("mango")
print("after :",fruits)

# insert is you to add an element at an specific index

colors = ["red","green","violet"]
print("before : ",colors)
colors.insert(2,"blue")
print("after : ",colors)

# remove is you to remove the value or character that match the first search case very well

number = [1,3,4,53,2,34,53,23,3242]
print("before : ",number)
number.remove(53)
print("after : ",number)

# pop removes and returns the elemetn at a specific index
stack = ["a","v","d"]
print("before : ",stack)
last_item = stack.pop()
print("last item is : ",last_item)
print("after : ",stack)

# with specific index
stack = ["a","v","d"]
print("before : ",stack)
last_item = stack.pop(1)
print("last item is : ",last_item)
print("after : ",stack)

# sort is use to sort the list items in place(asc order by default)

score = [34,64,21,33,45]
print("before : ",score)
score.sort()
print("after : ",score)

# same with descending 
score = [34,64,21,33,45]
print("before : ",score)
score.sort(reverse=True)
print("after : ",score)