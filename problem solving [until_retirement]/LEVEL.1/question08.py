n = int(input("Enter number: "))

rem_3 = n % 3
rem_5 = n % 5

if rem_3 == 0 and rem_5 == 0:
    print("divisible by 3 and 5")
else:
    print("not divisible by both")