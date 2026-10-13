# Question 24

n = int(input("Enter number: "))

is_negative = n < 0
if n < 0:
    n = -n

if n == 0:
    total = "0"
else:
    total = ""
    while n > 0:
        digit = n % 10
        total += str(digit)
        n //= 10

if is_negative:
    total = "-" + total

print(total)