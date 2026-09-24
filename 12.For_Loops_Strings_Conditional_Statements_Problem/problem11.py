# Problem 11

total_under = 0

for step in range(1):
    a = input("Enter user name:-").strip()

    if len(a) == 0:
        print("invalid") 

    length = len(a)
    first_char = a[0]

    score = 0
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    has_underscores = False

    for ch in a:
        if ch == "_":
            total_under += 1
            has_underscores = True
        elif ch.isdigit():
            has_digit = True
        elif ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif not ch.isalnum():
            has_special = True


    if length == 8:
        score += 1

    if "A" <= first_char <= "Z":
        score += 1

    if has_lower:
        score += 1

    if has_digit:
        score += 1

    if has_special:
        score += 1

    if score == 5:
        print("valid")
    else:
        print("invalid")

print(f"Total number of underscores={total_under}")



#  Aa12!@__