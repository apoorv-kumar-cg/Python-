# Question 10

og_pin = "1234"
attempts = 3

while attempts > 0:
    entered_pin = input("Enter your PIN: ")
    
    if entered_pin == og_pin:
        print("PIN accepted. Access granted!")
        break
        
    attempts -= 1
    if attempts > 0:
        print(f"Incorrect PIN. {attempts} attempt(s) remaining.")


else:
    print("Maximum attempts reached. Access is denied.")