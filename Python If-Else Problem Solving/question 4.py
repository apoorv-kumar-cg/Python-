a=int(input("Enter your 1st number="))
b=int(input("enter your 2nd number="))
c=int(input("enter your 3nd number="))

if a>b and a>c:
    print(f"{a} is greatest")
elif b>a and b>c:
    print(f"{b} is greatest")
elif c>b and c>a:
    print(f"{c} is greatest")
