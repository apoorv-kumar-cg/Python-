# Problem 11

row=1
while row<=5:
    col=1
    while col<=row:
        print(chr(64+col),end=" ")
        col+=1
    print()
    row+=1