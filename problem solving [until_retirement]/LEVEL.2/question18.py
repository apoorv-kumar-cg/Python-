# Question 18

N = int(input("Enter N: "))

count = 0
i = 1
while i <= N:
    if i % 3 == 0:
        count += 1
    i += 1

print(count)