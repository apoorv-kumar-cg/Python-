# Problem 3

sentence=input("Enter sentence :-")
a=sentence.replace(" ","")
# print(a)

score=0


for i in a:
    if i == "a" or  i == "e" or  i == "i" or  i == "o" or  i == "u" :
        score+=2
    elif "b"<= i >="d" or "f"<= i >="h" or "j"<= i >="n" or "p"<= i >="t" or "u"<= i >="z":
        score+=1 
    elif i.isdigit() :
        score+=3
    else:
        score+=4
    


print(f"total score is {score}")