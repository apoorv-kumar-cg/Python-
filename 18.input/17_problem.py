# Question 17

balance = 10000

while True:

    choice = input("""1. Check balance
2. Deposit money
3. Withdraw money
4. Exit
Enter your choice: """)
    
    if choice == "1":
        print(f"Balance: ${balance}")
    elif choice == "2":
        deposit = int(input("Enter Deposit money: "))
        if deposit > 0:
            balance += deposit
        else:
            print("Invalid amount")
    elif choice == "3": # Changed to string "3"
        withdraw = int(input("Enter withdraw money: "))
        if withdraw > balance or withdraw <= 0:
            print("Invalid")
        else:
            balance -= withdraw
            print(f"You withdrew: ₹{withdraw}")
    elif choice == "4": # Changed to string "4"
        print("it's over")
        break
    else:
        print("Invalid input")


    