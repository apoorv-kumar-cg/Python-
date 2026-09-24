# Problem 10

n = int(input("Enter n: "))

for row in range(1,n+1):
    for col in range(1,row+1):
        if col%3==0 and row%5==0:
            print("z",end=" ")
        elif col%3==0:
            print("x",end=" ")
        elif row%5==0:
            print("y",end=" ")
        else:
            print(row,end=" ")
    print()