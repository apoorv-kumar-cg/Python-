# Question 12

balance = 2000

while True:
    deposit = int(input("Enter deposit amount: $"))
    
    if deposit > 0:
        balance += deposit
        print(f"Deposit successful. New balance: ${balance}")
        break
    else:
        print("Invalid amount. Please enter a positive value greater than 0.\n")