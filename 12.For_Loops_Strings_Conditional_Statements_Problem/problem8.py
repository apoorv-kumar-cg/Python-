# Problem 8

total=0
budget=0
regular=0
premium=0
luxury=0
for i in range(8):
    a=int(input("Enter price:-"))
    total= total+a
    if a>5000:
       luxury+=1
    elif a>4999:
       premium+=1
    elif a>1999:
       regular+=1
    else:
       budget+=1

print(f"total price={total}")
print(f"average price={total/8}")
print(f"Budget product={budget}")
print(f"regular product={regular}")
print(f"Premium product={premium}")
print(f"Luxury product={luxury}")


