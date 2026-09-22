# Problem 4

for a in range(1,6):
    pas=input('ENTER PASSWORD:-')

a=len(pas)

score=0

for i in pas:
    if a==8:
        score+=1
    elif i.isupper():
        score+=1
    elif i.islower():
        score+=1
    elif i.isdigit():
        score+=1
    else:
        score+=1


if score==5:
    print("PASSWORD is strong")
elif score==[4,5]:
    print("PASSWORD is medium")
else:
    print("PASSWORD is weak")



