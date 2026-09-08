a=input("Username=")
b=input("Password=")

if a=="admin":
    if b=="python123":
        print("Login successful")
elif a!="admin":
    print("User not found")
elif b!="python123":
    print("Wrong password")

