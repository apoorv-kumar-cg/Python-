a = int(input("Enter 1st side="))
b = int(input("Enter 2nd side="))
c = int(input("Enter 3rd side="))


if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or c == a:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Invalid triangle")