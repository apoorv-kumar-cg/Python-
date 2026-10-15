# Question 19

while True:
    price = int(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    
    if price > 0 and quantity > 0:
        print(f"Final price: {price * quantity}")
        break  
    else:
        print("Invalid input. Both price and quantity must be greater than 0. Try again.\n")