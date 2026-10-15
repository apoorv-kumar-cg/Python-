# Question 23

one=int(input("Enter 1st score:-"))
avg=0

while True:
    # print("aaa")
    if 0<=one>=100:
      print("Redo!!!!!!!! ")
      one=int(input("Enter 1st score:-"))
    else:
    #    print("aaa")
       avg+=one
       break

two=int(input("Enter 2st score:-"))
# avg=0

while True:
    if 0<=two>=100:
      print("Redo!!!!!!!! ")
      two=int(input("Enter 2st score:-"))
    else:
       avg+=two
       break

three=int(input("Enter 3st score:-"))
# avg=0

while True:
    if 0<=three>=100:
      print("Redo!!!!!!!! ")
      three=int(input("Enter 3st score:-"))
    else:
       avg+=three
       break

print(f"The average of three number:-{avg/3}")

# [---------------------------------------------------------------------]

avg = 0

for i in range(1, 4):
    while True:
        score = int(input(f"Enter score {i}:- "))
        if 0 <= score <= 100: 
            avg += score
            break
        else:
            print("Redo!!!!!!!! ")

print(f"The average of three numbers:- {avg/3}")