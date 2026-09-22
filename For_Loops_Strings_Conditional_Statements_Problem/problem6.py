# Problem 6

odd=0
even=0
for i in range(5):
    a=input("Enter number:-")
    for j in a:
        if j == "1" or j == "3" or j == "5" or j == "7" or j == "9":
            odd+=1
        elif j == "2" or j == "4" or j == "6" or j == "8":
            even+=1

print(f"odd:={odd}")
print(f"even:={even}")


if odd>even:
    print("Odd occure most")
else:
    print("Even occure most ")