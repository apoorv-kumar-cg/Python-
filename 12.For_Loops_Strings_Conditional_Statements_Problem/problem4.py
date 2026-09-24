# Problem 4

for a in range(6):
    pas=input('ENTER PASSWORD:-')

a=len(pas)

score=0

for i in pas:
    if a>=8:
        score+=1
    elif "A"<=i<="Z":
        score+=1
    elif "a"<=i<="z":
        score+=1
    elif"1"<=i<="9":
        score+=1
    else:
        score+=1


if score==5:
    print("PASSWORD is strong")
elif score==[4,5]:
    print("PASSWORD is medium")
else:
    print("PASSWORD is weak")


# Apoorv1234@
