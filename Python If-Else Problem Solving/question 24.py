a=int(input("Original Price=="))

if a<500:
    print("discount=0%")
    print(f"Discount amount={0*a}")
    print(f"Final amount={(0*a)+a}")
elif a<999:
    print("discount=5%")
    print(f"Discount amount={5*a}")
    print(f"Final amount={(5*a)+a}")
elif a<1999:
    print("discount=10%")
    print(f"Discount amount={10*a}")
    print(f"Final amount={(10*a)+a}")
elif a<4999:
    print("discount=15%")
    print(f"Discount amount={15*a}")
    print(f"Final amount={(15*a)+a}")
elif a>5000:
    print("discount=20%")
    print(f"Discount amount={20*a}")
    print(f"Final amount={(20*a)+a}")