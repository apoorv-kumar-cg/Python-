# Problem 19

sentence = input("Enter sentence: ")

has_digit = False
has_url = False
has_at = False
has_password = False
has_repeated_special = False

# 1. Check for @ symbol
if "@" in sentence:
    has_at = True

# 2. Check for digits and repeated consecutive special characters
for i in range(len(sentence)):
    char = sentence[i]

    if char.isdigit():
        has_digit = True

    # Consecutive identical special characters (e.g. !!, ???, @@)
    if i < len(sentence) - 1:
        next_char = sentence[i + 1]
        if not char.isalnum() and not char.isspace():
            if char == next_char:
                has_repeated_special = True

# 3. Check for URL-like text and password-like patterns word by word
words = sentence.split()
for word in words:
    # URL-like text: contains '.' inside the word or starts with www / http
    if ("http://" in word or "https://" in word or "www." in word) or ("." in word and not word.endswith(".") and len(word) > 3):
        has_url = True

    # Password-like pattern: length >= 8 with combination of letters, digits, and special characters
    if len(word) >= 8:
        has_letter = False
        has_d = False
        has_s = False
        for c in word:
            if c.isalpha():
                has_letter = True
            elif c.isdigit():
                has_d = True
            elif not c.isalnum():
                has_s = True
        if has_letter and has_d and has_s:
            has_password = True

# Count how many risk indicators were detected
risk_count = 0
if has_digit:
    risk_count += 1
if has_url:
    risk_count += 1
if has_at:
    risk_count += 1
if has_password:
    risk_count += 1
if has_repeated_special:
    risk_count += 1

# Classification:
# 0 flags -> Safe
# 1-2 flags -> Review
# 3 or more flags -> Suspicious
if risk_count == 0:
    print("Safe")
elif risk_count <= 2:
    print("Review")
else:
    print("Suspicious")
