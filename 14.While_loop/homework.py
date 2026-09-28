
i=1
while i<6:
    print("Hello")
    i+=1


i=0
while i<10:
    print(i,end=" ")
    i+=1


i=1
while i<11:
    print(i)
    i+=1


i=1
while i<11:
    print(11-i)
    i+=1

#5
i=5
while i<51:
    print(i)
    i+=5

#6
i=2
while i<21:
    print(i)
    i+=2

#7
i=1
while i<20:
    print(i)
    i+=2

#8
i=3
while i<19:
    print(i,end=" ")
    i+=3

#9
i=20
while i>=2:
    print(i)
    i-=2

#10
n=int(input("Enter number:"))
i=1
while i<n+1:
    print(i)
    i+=1

#11
n=int(input("Enter number:"))
i=2
while i<n+1:
    print(i)
    i+=2

#12
n=int(input("Enter number:"))
i=1
while i<n+1:
    print(i)
    i+=2

#13
n=int(input("Enter number:"))
i=1
while i<n+1:
    if i%3==0:
        print(i)
    i+=1

#14
n=int(input("Enter number:"))
i=1
while i<n+1:
    if i%3==0 and i%2==0:
        print(i)
    i+=1

#15
n=int(input("Enter number:"))
i=1
even_count=0
while i<n+1:
    if i%2==0:
        even_count+=1
    i+=1
print(even_count)    

#16
n=int(input("Enter number:"))
i=1
total=0
while i<n+1:
    total+=i
    i+=1
print(total)

#17
n=int(input("Enter number:"))
i=1
total=0
while i<n+1:
    if i%2==0:
        total+=i
    i+=1
print(total)

#18
n=int(input("Enter number:"))
i=1
total=0
while i<n+1:
    if i%2!=0:
        total+=i
    i+=1
print(total)

#19
n=int(input("Enter number:"))
i=1
while i<11:
    print(i*n)
    i+=1

#20
n=int(input("Enter number:"))
i=1
fac=1
while i<n+1:
    fac*=i
    i+=1
print(fac)    

#21
string=input("Enter string:")
i=0
while i<len(string):
    print(string[i])
    i+=1

#22
string=input("Enter string:")
i=0
while i<len(string):
    print(string[i],end="")
    i+=1

#23
string=input("Enter string:")
i=0
char_count=0
while i<len(string):
    char_count+=1
    i+=1
print(char_count)    

#24
string=input("Enter string:")
i=0
a_count=0
while i<len(string):
    if string[i]=="a":
        a_count+=1
    i+=1
print(a_count)    






