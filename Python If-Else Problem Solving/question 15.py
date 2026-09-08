cp=int(input("Enter cost price="))
sp=int(input("Enter selling price="))

if sp>cp:
    print(f"Profit is {sp-cp}")
elif cp>sp:
    print(f"LOSS is {cp-sp}")
elif cp==0 and sp==0:
    print("Enter correctly")
elif cp==sp:
    print("no profit no loss")
