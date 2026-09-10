# for i in range(12, 0, -1):
#     print(i)

str=input("enter a word=").strip().lower()
str2=""
length=len(str)
for a in range(length-1,-1,-1):
    str2=str2+str[a]
if str==str2:
    print("OK")
else:
    print("NOT OK")
