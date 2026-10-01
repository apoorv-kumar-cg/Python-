n=int(input("Enter number:="))
i=1
count=0
while i<=n:
    if i%2==0:
     count+=1
    i+=1

print(f"Total no of even number is {count}")