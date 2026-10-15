# Question 9

num=int(input("Enter which /3 and /5:-"))
count=0

while True:
    if num%3==0 and num%5==0:
        count+=1
        print("Divisible by 3 and 5")
        print(f"Total count:-{count}")
        
        break
    else:
        num=int(input("Enter which /3 and /5:-"))
        count+=1