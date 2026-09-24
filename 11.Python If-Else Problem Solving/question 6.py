a=int(input("enter your number="))


if a%5==0 and a%11==0:
     print("DIVISIBLE BY both 5 and 11")
elif a%5==0:
    print("DIVISIBLE BY 5")
elif a%11==0:
     print("DIVISIBLE BY 11")
else:
     print("NOT DIVISIBLE BY BOTH 5 AND 11")
