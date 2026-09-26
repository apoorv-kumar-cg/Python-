# Problem 12

a=65

for row in range(1,6):
    for col in range(row):
        print(chr(a),end=" ")
    print()
    a+=1