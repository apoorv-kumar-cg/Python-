a=int(input("enter your age="))

if a<=0:
    print("Invalid age")
elif a<18:
    print("Can't vote")
elif a>=18:
    print("can vote")
else:
    print("Enter correct age")