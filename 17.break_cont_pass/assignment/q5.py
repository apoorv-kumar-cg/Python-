text = input("Enter string: ")
target = input("Enter target character: ")

for char in text:
    print(char, end=" ")
    if char == target:
        break