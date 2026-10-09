# Question 21

n=int(input("Enter number:-"))

if n<0:
    n=-n
if n==0:
    count=1
else:
    count=0
    while n>0:
        count+=1
        n=n//10
print(count)
