n=int(input("Enter number:="))
i=1
count=0
while i<=n:
    if i%2!=0:
     count+=i
    i+=1
print(count)