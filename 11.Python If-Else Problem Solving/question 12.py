ch=input("enter=")[0].strip().lower()
if "A"<= ch <="Z":
    print("uppercase Alphabate")
elif "a"<= ch <="z":
    print("Lowercase alphabet")
elif 0 <= int(ch) <= 9j:
    print("Digit")
else:
    print("Special character")
