marks = int(input("Enter:").split())
for mark in marks:
    if mark < 40:
        continue
    print(mark, end=" ")