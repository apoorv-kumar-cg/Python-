# Question 23

n = int(input("Enter number: "))

if n < 0:
    n = -n

if n == 0:
    total = 0
else:
    total = 1
    while n > 0:
        digit = n % 10
        total *= digit
        n //= 10

print(total)
    