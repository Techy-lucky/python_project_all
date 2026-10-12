marks = int(input("please enter your marks : "))
if( marks >= 100):
    print("that score is doesnot exists")
elif(marks >= 90):
    print("you have an O grade in your score")
elif(marks >= 80):
    print("you have an A+ grade in your score")
elif(marks >= 70):
    print("you have an A grade in your score")
elif(marks >= 60):
    print("you have an B+ grade in your score")
elif(marks >= 50):
    print("you have an B grade in your score")
elif(marks >= 40):
    print("you have an C+ grade in your score")
elif(marks >= 35):
    print("you have an C grade in your score")
elif(marks <=34 or marks >=0):
    print("you have fail in your grade")
else :
    print("no negative are allowed")
