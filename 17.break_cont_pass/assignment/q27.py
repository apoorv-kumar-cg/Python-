word = input("Enter:-")
for ch in word:
    if word.count(ch) >= 2:
        print(ch)
        break
else:
    print("No repeated character")