n=input("Enter Number=").lower()
i=0
length=len(n)
char=0
while i<length:
    if n[i]=="a":
        char+=1
    i+=1

print(char)

