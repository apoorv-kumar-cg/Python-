a=int(input("enter your number="))


if a%3==0 and a%7==0:
     print("DIVISIBLE BY both 3 and 7")
elif a%3==0:
    print("DIVISIBLE BY 3")
elif a%7==0:
     print("DIVISIBLE BY 7")
else:
     print("NOT DIVISIBLE BY BOTH 3 AND 7")
