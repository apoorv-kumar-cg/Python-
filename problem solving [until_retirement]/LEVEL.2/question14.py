# Question 14

N = int(input("Enter N: "))

i = 1
while i <= N:
    if (i & 1) != 0:
        print(i, end=" ")
    i += 1
print()