# Question 25

a=int(input("Enter number:-"))
total=""
while a>0:
    digit=a%10
    digit=str(digit)
    total+=digit
    a=a//10
# print(total)

if total==a:
   print("palindrome")
else:
    print("not palindrome")