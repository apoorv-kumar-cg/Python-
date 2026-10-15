word= input("Enter sentence:-").split()
target= input("Enter traget word:-").split()
for ch in word:
    if ch == target:
        print("Character exists")
        break
else:
    print("Character missing")