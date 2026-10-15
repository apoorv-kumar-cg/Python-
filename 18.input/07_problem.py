# Question 7

balance=5000
a=int(input("Enter withdrawl amount:-"))

while True:
    if a>=5000:
        print("Input invaid")
        a=int(input("Enter withdrawl amount:-"))
    elif a<=5000:
        print("Valid")
        break


