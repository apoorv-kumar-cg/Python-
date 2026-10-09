# Question 19

N = int(input("Enter N: "))

fact = 1
i = 1
while i <= N:
    fact *= i
    i += 1

print(fact)