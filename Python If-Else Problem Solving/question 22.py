a=int(input("Account balance="))
b=int(input("Withdrawal amount="))

if b>0 and b%100==0 and a-b>=500:
     print("Withdrawal successful.")
     print(f"Remaining Balance {a-b}")
else:
    print("Withdrawal Unsuccessful!!!!ENTER CORRECT DATA!!!")
