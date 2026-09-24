hour=int(input("Enter hour="))
minute=int(input("Enter min="))
second=int(input("Enter sec="))

if 1<=hour<=24:
    if 1<=minute<=59:
        if 1<=second<=59:
            print("Valid")
else:
    print("invalid")