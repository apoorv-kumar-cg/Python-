# Problem 17

mark=0
for i in range (5):
    name=input("enter name= ")
    for j in range (5):
        markS=int(input("enter mark out of 20:- "))
        mark+=markS
        print(mark)

    
    if mark<50:
        print("Grade=D")
    elif mark<70:
        print("Grade=C")
    elif mark<80:
         print("grade=B")
    else:
        print("Grade=A")


