# Question 11

while True:

    number = int(input("Enter an integer between 10 and 50: "))
    
    if 10 <= number <= 50:
        if number % 2 == 0:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
        break
    else:
        print("Number out of range. Please try again.")
        print("Invalid input. Please enter a valid integer.")
            

        