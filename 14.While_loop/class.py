# n=int(input("Enter a number="))

# while n!=0:
#     print(f"Given num= {n}")
#     n=int(input("Enter a number="))

# print("Loop ended")

number = int(input("Enter a number: "))

total = 0

while number != 0:
    total = total + number
    number = int(input("Enter a number: "))

print("Sum:", total)


