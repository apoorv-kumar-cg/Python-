# Question 8

username=input("Enter:=")
# username=username.replace(" ","")

while True:
    if len(username)>5:
        for i in username:
            if i!=" ":
                print("Valid")
                break
    else:
        username=input("Enter:=")