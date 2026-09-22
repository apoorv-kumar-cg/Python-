s = input("Enter string: ")

upper = 0
lower = 0
digit = 0
space = 0
special = 0

for char in s:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    elif char.isdigit():
        digit += 1
    elif char == " ":
        space += 1
    else:
        special += 1

print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
print(f"Digits: {digit}")
print(f"Spaces: {space}")
print(f"Special characters: {special}")


