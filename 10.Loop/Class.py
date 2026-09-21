# for i in range(12, 0, -1):
#     print(i)

# str=input("enter a word=").strip().lower()
# str2=""
# length=len(str)
# for a in range(length-1,-1,-1):
#     str2=str2+str[a]
# if str==str2:
#     print("OK")
# else:
#     print("NOT OK")


# for i in range(4):
#     for j in range(6):
#         print(i*j)

# for row in range(5):
#     for colomn in range (9):
#         print("*",end="")
#     print()

# for row in range(4):
#     for colomn in range (40):
#         print("*",end="")
#     print("")

# for i in range (4):
#     print("****")

# for row in range(10,0,-1):
#     for colmn in range(row):
#         print("1",end="")
#     print()

# a=int(input("Enter a digit="))

# for i in range(a):
#     bag=""
#     for j in range(i+1):
#         bag+=str(j+1)
#     print(bag)

# for i in range (1,a+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# a=int(input("Enter a digit="))

# for i in range(1,a+1):
#     for j in range(1,(a+1)-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end="")
#     print()

# for i in range(6,0,-1):
#     for j in range(1,7-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end="")
#     print()

# total=0
# flag=True
# grade=" "

# for i in range (5):
#     marks=int(input("Enter mark:="))
#     total+=marks

#     if marks<35:
#         flag=False
# percent=total/5

# if flag==True:
#     if percent>=90:
#         grade="A+"
#     elif percent>=80:
#         grade="A"
#     elif percent>=70:
#         grade="B"
#     elif percent>=60:
#         grade="C"
#     elif percent>=50:
#         grade="D"
#     elif percent<50:
#         grade="F"
# else:
#     print("You're Fail")

# print(f"Your Total Marks={total}")
# print(f"Your Total percent={percent}")
# if flag==True:
#   print(f"Your Grade={grade}")



total=0
mem=input("Are you a member(Yes/no)=").lower().strip
discount=""
final_price=""


for i in range(5):
    price=int(input("Enter price="))
    total=total+price
    print(total)

if mem=="yes":
    if total>=5000:
        discount="25%"
        final_price=(total-(total/0.25))
    elif total>=2000:
        discount="15%"
        final_price=(total-(total/0.15))
    elif total>=1000:
        discount="10%"
        final_price=(total-(total/0.1))
elif mem=="no":
    if total>=5000:
        discount="20%"
        final_price=(total-(total/0.20))
    elif total>=2000:
        discount="10%"
        final_price=(total-(total/0.10))
    elif total>=1000:
        discount="5%"
        final_price=(total-(total/0.05))

print(discount)
print(final_price)
