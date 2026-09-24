# Problem 18

deposite=0
withdrawal=0
score=0

for i in range(2):
    a=int(input("Enter Deposite Amount="))
    deposite+=a
    b=int(input("Enter Withdrawal Amount="))
    withdrawal+=b

    if withdrawal>deposite:
        print("Not suficient balance")
    elif deposite<1000:
        print("Gariiiib")
    else:
       print(f"Update balance={deposite-withdrawal}")
       score+=1


print(deposite)
print(withdrawal)
print(f"Total number of transition= {score}")