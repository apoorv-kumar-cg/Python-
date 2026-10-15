# Question 6

while True:
    
        temp = int(input("Enter a temperature between -20 and 45: "))
        
        if -20 <= temp <= 45:
            print(f"Valid temperature entered: {temp}")
            break
        else:
            print("Temperature out of range. Please try again.\n")
            
