# Question 16

a=int(input("Enter 1st number:-"))
b=int(input("Enter 2st number:-"))
c=input("Enter:-\n(+) for Addition:-\n (-) for subtraction:-\n(*)for multiply:-\n(/)for divide:-")

if c=="+":
    print(a+b)
    # break

if c=="-":
    print(a-b)
    # break

if c=="*":
    print(a*b)
    # break

while True:
    if c=="/":
        if b ==0:
            b=int(input("Enter 2st number:-"))
        else:
            print(a/b)
            break

