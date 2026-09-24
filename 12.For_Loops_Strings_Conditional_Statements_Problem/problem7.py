text =input("Enter:-")

# Track already processed characters to avoid duplicate checks
seen = ""

for char in text:
    # Check if the character has already been evaluated
    if char in seen:
        pass
    else:
        seen += char

        # Count occurrences manually using a nested loop
        count = 0
        for current in text:
            if current == char:
                count += 1

        # Classify and print based on frequency
        if count == 2:
            print(f"'{char}' -> Duplicate ({count} times)")
        elif 3 <= count <= 4:
            print(f"'{char}' -> Repeated ({count} times)")
        elif count > 4:
            print(f"'{char}' -> Highly Repeated ({count} times)")
        else:
            pass