# Question 4

while True:
    print("1. View profile")
    print("2. Edit profile")
    print("3. Settings")
    print("4. Exit")
    
    choice=input("Enter your choice (1, 2, 3, or 4): ")
    
    if choice in ['1', '2', '3', '4']:
        print(f"You selected option {choice}.")
        break
    else:
        print("Invalid choice. Please try again.")