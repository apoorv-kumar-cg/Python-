a=input("enter character=")[0].strip().lower()

if a=="a" or a=="e" or a=="i" or a=="o" or a=="u":
    print("Vowel")
elif "b"<= a <="d" or "f" <= a <= "h" or "j" <= a <= "n" or "p" <= a <= "t" or "v" <= a <= "z":
    print("Consonant")
else:
    print("Invalid input")