# Question 21


while True:
    password=input("Enter the password:-")
    i=0

    if len(password)>8:
        i=i+1
    else:
        print("Password length is not 8 or greater")
       

    for i in password:
        if i.isdigit():
            i=i+1
            break
        else:
            print("Digit is missing")

    for i in password:
        if i.isupper():
            i=i+1
            break
        else:
            print("Uppercase is missing")
    for i in password:
        if i.islower():
            i=i+1
            break
        else:
            print("lower is missing")

    space=False
    for i in password:
        if i ==" ": 
          space=True
          i=i+1
          break

    if space==False:
        print("Space is missing")

    if i==5:
        print("password is valid")
        break
    else:
        print("password is invalid")


    



# while True:
#     password = input("Enter the password:- ")
    
#     # 1. Reset score to 0 for every new attempt
#     score = 0  
    
#     # 2. Check length (must be >= 8 to get a point)
#     if len(password) >= 8:
#         score = score + 1
#     else:
#         print("- Password is less than 8 characters")

#     # 3. Check for a digit
#     for char in password:
#         if char.isdigit():
#             score = score + 1
#             break
#     else:
#         print("- Missing a digit")

#     # 4. Check for uppercase
#     for char in password:
#         if char.isupper():
#             score = score + 1
#             break
#     else:
#         print("- Missing an uppercase letter")
        
#     # 5. Check for lowercase
#     for char in password:
#         if char.islower():
#             score = score + 1
#             break
#     else:
#         print("- Missing a lowercase letter")

#     # 6. Check for whitespace (from your original requirements)
#     has_space = False
#     for char in password:
#         if char.isspace():
#             has_space = True
#             break
            
#     if not has_space:
#         score = score + 1
#     else:
#         print("- Contains whitespace")

#     # Final Check: If it passed all 5 rules, break the loop
#     if score == 5:
#         print("Password valid!")
#         break
#     else:
#         print("Please try again.\n")

    

