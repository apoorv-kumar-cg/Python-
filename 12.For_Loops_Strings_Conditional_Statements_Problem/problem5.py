# Problem 5

sen=input("Enter sentence:-").split()

for i in sen:
    i=len(sen)
    if i <=3:
        print("short")
    elif i <=5:
        print("Medium")
    else:
        print("Long")



