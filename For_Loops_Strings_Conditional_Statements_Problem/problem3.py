# Problem 3

sentence=input("Enter sentence :-")
a=sentence.replace(" ","")
# print(a)

vowel=0
consonant=0
Digit=0
special=0
score=0


for i in a:
    if i == "a" or  i == "e" or  i == "i" or  i == "o" or  i == "u" :
        vowel+=2
        score+=2
    elif "b"<= i >="d" or "f"<= i >="h" or "j"<= i >="n" or "p"<= i >="t" or "u"<= i >="z":
        consonant+=1 
    elif i == :
        Digit+=3
        score+=1 
    elif i.isdigit() :
        score+=3
    else:
        special
        score+=4
    


print(consonant)
print(f"total score is {score}")