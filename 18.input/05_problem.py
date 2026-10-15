# Question 5

while True:
    password=input("Enter password:-")
    password=password.replace(" ","")
    if len(password)>8:
        print("Valid")
        break
    else:
        print("invalid")
        password=input("Enter password:-")


