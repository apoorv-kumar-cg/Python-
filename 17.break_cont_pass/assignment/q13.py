word, char = input("Enter:-").split()
for ch in word:
    if ch == char:
        continue
    print(ch, end="")