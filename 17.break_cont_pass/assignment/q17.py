word = input("Enter:-")
count = 0
for ch in word:
    if ch in "aeiou":
        continue
    count += 1
print(count)