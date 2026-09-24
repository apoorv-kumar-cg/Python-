# Problem 15

a=""
b=""
c=""
even=0
odd=0
positive=0
nigative=0
zero=0

for row in range(3):

    a=int(input("Enter one:-"))
    b=int(input("Enter two:-"))
    c=int(input("Enter three:-"))


    if a%2==0:
        even+=1
    elif a%2!=0:
        odd+=1
    elif a>0:
        positive+=1
    elif a<0:
        nigative+=1
    elif a==0:
        zero+=1

    if b%2==0:
        even+=1
    elif b%2!=0:
        odd+=1
    elif b>0:
        positive+=1
    elif b<0:
        nigative+=1
    elif b==0:
        zero+=1

    if c%2==0:
        even+=1
    elif c%2!=0:
        odd+=1
    elif c>0:
        positive+=1
    elif c<0:
        nigative+=1
    elif c==0:
        zero+=1


print(f"Even count= {even}")
print(f"add count= {odd}")
print(f"positive count= {positive}")
print(f"negative count= {nigative}")
print(f"zero count= {zero}")




