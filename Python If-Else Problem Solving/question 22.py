a=int(input("Account balance="))
b=int(input("Withdrawal amount="))

if b>0:
    if b%100==0:
        if b<a:
            if b-a==500:
                print("Withdrawal successful")
else:
    print("Withdrawal Unsuccessful")