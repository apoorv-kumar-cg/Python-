a = int(input("Enter your age: "))
id = input("Do you have an ID?").strip().lower()

if a >= 18 and id == "yes":
    print("allowed")
else:
    print("not allowed")
