a=int(input("Original Price=="))

if a<500:
    print(f"original amount={a}")
    print("discount=0%")
    print(f"Discount amount={0*a}")
    print(f"Final amount={a-(0*a)}")
elif a<999:
    print(f"original amount={a}")
    print("discount=5%")
    print(f"Discount amount={.05*a}")
    print(f"Final amount={a-(.05*a)}")
elif a<1999:
    print(f"original amount={a}")
    print("discount=10%")
    print(f"Discount amount={.10*a}")
    print(f"Final amount={a-(.10*a)}")
elif a<=4999:
    print(f"original amount={a}")
    print("discount=15%")
    print(f"Discount amount={.15*a}")
    print(f"Final amount={a-(.15*a)}")
elif a>=5000:
    print(f"original amount={a}")
    print("discount=20%")
    print(f"Discount amount={.20*a}")
    print(f"Final amount={a-(.20*a)}")