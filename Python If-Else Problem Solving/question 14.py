cp=int(input("Enter cost price="))
sp=int(input("Enter selling price="))

if sp>cp:
    print("Profit")
elif cp>sp:
    print("LOSS")
else:
    print("no profit no loss")
