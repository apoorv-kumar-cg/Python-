a=int(input("Enter 1st side="))
b=int(input("Enter 2nd side="))
c=int(input("Enter 3ed side="))

if a+b==c or a+c==b or b+c==a:
    print("valid triangle")
else:
    print("Invalid triangle")