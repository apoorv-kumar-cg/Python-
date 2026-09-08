a=int(input("Enter electricity units="))

if a<=100:
    print(f"Bill is {a*5}")
elif a<=200:
    print(f"Bill is {a*7}")
elif a>200:
    print(f"Bill is {a*10}")