# Problem 21

item=0
total=0
dis=0
for i in range(10):
    a=int(input("enter price= "))


    if a>=5000:
        item+=1
        dis+=(a*0.2)
        total+=a-(a*0.2)
    elif a>=3000:
        item+=1
        dis+=(a*0.15)
        total+=a-(a*0.15)
    elif a>=1000:
        item+=1
        dis+=(a*0.1)
        total+=a-(a*0.1)
    else:
        print(f"Final Price= {a}")
        print("NO DISCOUNTTTT")

print(f"total no of item resive discount={item}")
print(f"Total discount= {dis}")
print(f"Final Price= {total}")