# Question 13

while True:
    number = int(input("Enter an integer between 1 and 100: "))
    
    if 1 <= number <= 100:
        print(f"Valid number entered: {number}")
        break
    else:
        print("Number out of range. Please try again.\n")