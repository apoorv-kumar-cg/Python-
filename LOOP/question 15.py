n=input("Enter Number=")
for a in range(0,n):
    b=a.len()
    print(a)
   
n = int(input("Enter number: "))

count = 0
for i in range(1, n + 1):
    if i % 2 == 0 and i % 2 != 0:
        count += 1

print(f"Total even numbers from 1 to {n}: {count}")