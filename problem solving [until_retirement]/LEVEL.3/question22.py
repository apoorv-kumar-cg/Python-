# Question 22

n=int(input("Enter number:-"))

if n<0:
    n=-n
total=0

while n>0:
    digit=n%10
    total+=digit
    n=n//10
print(total)