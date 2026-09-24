# Problem 16

s = input("Enter string: ")

upper = 0
lower = 0
digit = 0
special = 0

for char in s:
    if "A"<=char<="Z":
        upper += 1
    elif "a"<=char<="z":
        lower += 1
    elif "1"<=char<="9":
        digit += 1
    else:
        special += 1

print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
print(f"Digits: {digit}")
print(f"Special characters: {special}")

length=len(s)

print(f"percentage of uppercase letter= {(length/upper)*100}")
print(f"percentage of lowerrcase letter= {(length/lower)*100}")
print(f"percentage of digitr= {(length/digit)*100}")
print(f"percentage of special characters= {(length/special)*100}")
