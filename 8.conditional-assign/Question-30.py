age = int(input("Enter age: "))
marks = int(input("Enter marks: "))
has_id = input("Do you have an ID? (yes/no): ").strip().lower() 

if age >= 18 and marks >= 40 and has_id=="yes":
    print("Eligible")
else:
    print("Not eligible")


    a