# Question 18

while True:
    month = int(input("Enter a month number (1-12): "))
    day = int(input("Enter a day number (1-31): "))
    

        
    if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"Success! You entered Month: {month}, Day: {day}")
            break
    else:
            print("Error: Month must be between 1-12 and day between 1-31.\n")
