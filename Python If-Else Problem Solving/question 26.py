day = int(input("Day="))
month = int(input("Month="))
year = int(input("Year="))

if year >= 1 and 1 <=month <= 31:
    leap=(year%4==0 and year%100!=0) or (year%400==0)

    if month in (1,3,5,7,8,10,12):
        maxday = 31
    elif month in (4,6,9,11):
        maxday = 30
    elif leap:
        maxday = 29
    else:
        maxday = 28

    if 1<= day <= maxday:
        print("valid")
    else:
        print("Invalid")
else:
    print("Invalid")


