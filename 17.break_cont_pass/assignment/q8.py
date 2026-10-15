sentence = input("enter:-").split()
target = input("enter:-")
for word in sentence:
    if word == target:
        print("Found")
        break
else:
    print("Not found")