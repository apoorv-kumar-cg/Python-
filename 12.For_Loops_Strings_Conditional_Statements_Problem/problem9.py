# Problem 9

a=input("Enter=")

for i in a:
    for j in range(len(a)):
        if j%2==0:
            pos="even"
        else:
            pos="odd"

        print(f"position of {i} in word is {j} and position is {pos}")

    
