# Question 26

num=int(input("Enter number:-"))

for i in range(2,num):
    if num%i==0:
        print("Not prime")
        break
    else:
        print("prime")
        break

if num==2:
    print("Prime")
if num==1:
    print("Not prime nor composite")