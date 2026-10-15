# Question 20

times=int(input("How many number you wanna to enter:-"))
count=0

for i in range(times):
    num=int(input("Enter the number:-"))
    count+=num
print(f"Average:- {count/times}")