# Problem 23

for i in range(8):
    a=int(input("enter salary= "))

    if a>100000:
        print("Executive")
    elif a<100000:
        print("Senior")
    elif a>50000:
        print("mid")
    elif a<25000:
        print("junior")
    print()

