# Problem 12

a=input("Enter sentence:-").lower()
b=a.replace(" ","")

vol=0
con=0

for i in b:
    if i == "a" or  i == "e" or  i == "i" or  i == "o" or  i == "u" :
        vol+=1
    if "b"<= i >="d" or "f"<= i >="h" or "j"<= i >="n" or "p"<= i >="t" or "u"<= i >="z":
        con+=1


print(f"total number of vowel={vol}")
print(f"total number of consonant={con}")

if vol>con:
    print("Consonants win")
elif vol==con:
    print("Draw")
else:
    print("Vowels win")