a=int(input("Enter your AGE="))
b=int(input("enter your AGE="))
c=int(input("enter your AGE="))

if a<b and a<c:
    print("1st is youngest")
elif b<a and b<c:
    print("2nd is youngest")
elif c<b and c<a:
    print("3rd is youngest")
elif a==b:
    print("1st and 2nd are equal")
elif b==c:
    print("2st and 3nd are equal")
elif c==a:
    print("3st and 1nd are equal")
elif a==b==c:
    print("All are equal")




