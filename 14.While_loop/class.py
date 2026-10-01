# n=int(input("Enter a number="))

# while n!=0:
#     print(f"Given num= {n}")
#     n=int(input("Enter a number="))

# print("Loop ended")

# number = int(input("Enter a number: "))

# total = 0

# while number != 0:
#     total = total + number
#     number = int(input("Enter a number: "))

# print("Sum:", total)

#[------------------------------------------]

# password = input("Enter Password: ")

# while password!="Vtwzknn1234@":
#     print("WRONG PASSWORD")
#     password = input("Enter Password: ")

# print("CORRECT PASSWORD")

# word=input("Enter=").lower().strip()

# length=len(word)
# opp_word=word[::-1]

# while word!=opp_word:
#     print("Not correct")
#     word=input("Enter=").lower().strip()

# print("Correct")

#[---------------------------------------------]

# word=input("Enter=").lower().strip()

# length=len(word)
# opp_word=""

# i=length-1

# while i>=0:
#     opp_word+=word[i]
#     i-=1

# if word==opp_word:
#     print("Correct")
# else:
#     print("Incorrect")

#[--------------------------------------------------]

# word=input("Enter=").lower().strip()
# i=0
# j=len(word)-1
# flag=True

# while i<j:
#     if word[i]==word[j]:
#      i+=1
#      j-=1
#     else:
#        flag=False
#        i=j

# if flag==True:
#     print("Correct")
# else:
#     print("Incorrect")

#[-----------------------------------------------------]

# number=int(input("Enter:-"))
# total=0

# while number>0:
#     digit=number%10
#     total+=digit
#     number=number//10
# print(total)

#[-----------------------------------------------------]

# number=int(input("Enter:-"))

# reversed=0
# while number>0:
#     digit=number%10
#     reversed=reversed*10+digit
#     number=number//10
# print(reversed)

# reversed=""
# while number>0:
#     digit=number%10
#     digit=str(digit)
#     reversed+=digit
#     number=number//10
# print(reversed)


#[-----------------------------------------------------]

# row=1

# while row <=3:
#     col=1

#     while col<=5:
#         print("*",end="")
#         col+=1
#     print()
#     row+=1

#[-----------------------------------------------------]

# row=1

# while row<=5:
#     col=row

#     while col<=5:
#         print(col,end="")
#         col+=1
#     print()
#     row+=1

#[-----------------------------------------------------]

# row=1

# while row<=5:
#     col=1

#     while col<=row:
#         print(col,end="")
#         col+=1
#     print()
#     row+=1

#[-----------------------------------------------------]

