a = int(input("Enter 1st sub mark=="))
b = int(input("Enter 2nd sub mark=="))
c = int(input("Enter 3rd sub mark=="))

if 0<=a<=100 and 0<=b<=100 and 0<=c<=100:
    if a >= 35 and b >= 35 and c >= 35:
        d = (a + b + c) / 3
        if d >= 75:
            print("Distinction")
        elif d >= 60:
            print("First class")
        elif d >= 50:
            print("Second class")
        else:
            print("Pass")
    else:
        print("Fail")
else:
    print("Invalid marks")
    