text = input("Enter a string: ")

count = 0
i = 0

while i < len(text):
    if text[i].isupper():
        count += 1
    i += 1

print("Total uppercase letters:", count)