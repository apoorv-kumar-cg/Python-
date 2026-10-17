# Q-1

# def welcome():
#     print("Welcome to Python")

# welcome()
# welcome()
# welcome()

# [------------------------------------------------------------------]

# Q-2

# def greet(name):
#     print("Hello" , name)

# greet("Apoorv")

# [------------------------------------------------------------------]
# Q-3

# def show_number(number):
#     print(number)

# print(3452)

# [------------------------------------------------------------------]
# q-4

# def add(a,b):
#     return a+b
# print(add(12,44))


# [------------------------------------------------------------------]

# Q-5

# def square(a):
#     return a**2

# print(square(12))

# [------------------------------------------------------------------]

# Q-6

# def full_name(first, last):
#     return first+" "+last

# print(full_name("Apoorv", "Kumar"))

# [------------------------------------------------------------------]
# Q-7

# def introduce(name, city="Pune"):
#     return name,city
# print(introduce("Apoorv"))

# [------------------------------------------------------------------]

# Q-8

# def introduce(name, city="Pune"):
#     print(f"My name is {name} and I am from {city}.")

# introduce("raj")

# introduce("apoorv", "bihar")

# [------------------------------------------------------------------]
# Q-9

# def subtract(a, b):
#     return a - b

# result_1 = subtract(100, 50)
# print(result_1)

# result_2 = subtract(50, 100)
# print(result_2)

# [------------------------------------------------------------------]
# Q-10

# def get_min_max(a, b):
#     return min(a, b), max(a, b)

# result_1 = get_min_max(15, 8)
# print(result_1)

# result_2 = get_min_max(4, 20)
# print(result_2)

# [------------------------------------------------------------------]
# q-11
# def cal(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)

# print(cal(10,1))



# [------------------------------------------------------------------]
# q-12
# def count_digits(number):
#     point = 0
#     for i in str(number):
#         if i.isdigit():
#             point += 1
#     print(f"Total number of digit is {point}")

# count_digits(12345)

# [------------------------------------------------------------------]
# q-13

# def classify_number(n):
#     return "Positive" if n > 0 else "Negative" if n < 0 else "Zero"

# print(classify_number(15))
# print(classify_number(-8))
# print(classify_number(0))

# [------------------------------------------------------------------]
# q-14

# def calculate_total(price, quantity=1):
#     return price * quantity

# print(calculate_total(100))
# print(calculate_total(100,9))

# [------------------------------------------------------------------]
# q-15
# def create_email(username, domain="example.com"):
#     return f"{username}@{domain}"

# print(create_email("user"))
# print(create_email("admin", "company.org"))

# [------------------------------------------------------------------]
# # q-16

# def format_name(first, last, uppercase=False):
#     full_name = f"{first} {last}"
#     return full_name.upper() if uppercase==True else full_name

# print(format_name("apoorv", "kumar"))
# print(format_name("apoorv", "kumar", uppercase=True))

# [------------------------------------------------------------------]
# q-17

# def percentage(marks, total=100):
#     return (marks / total) * 100

# print(percentage(85))
# print(percentage(45, 50))

# [------------------------------------------------------------------]
# q-18

# def convert_minutes(minutes, seconds_per_minute=60):
#     return minutes * seconds_per_minute

# print(convert_minutes(5))

# [------------------------------------------------------------------]
# q-19

# def student_details(name, age, city):
#     print(f"Name: {name}, Age: {age}, City: {city}")

# student_details(city="Delhi", name="Rahul", age=20)

# [------------------------------------------------------------------]
# q-20
# def bill(item, quantity=1, price=100):
#     return quantity * price

# print(bill("Pen"))
# print(bill("Notebook", 2, 50))
# print(bill(price=200, item="Bag", quantity=3))

# [------------------------------------------------------------------]


# Q-21
# def analyze_number(number):
#     val = -number if number < 0 else number
#     is_even = number % 2 == 0
#     digit_count = len(str(abs_val))
#     return val, is_even, digit_count

# print(analyze_number(-1234))
# print(analyze_number(560))

# # [------------------------------------------------------------------]

# # Q-22
# def calculate_stats(a, b, c):
#     smallest = min(a, b, c)
#     largest = max(a, b, c)
#     total = a + b + c
#     return smallest, largest, total

# print(calculate_stats(10, 5, 20))

# # [------------------------------------------------------------------]

# # Q-23
# def make_sentence(subject, verb, object):
#     return f"{subject} {verb} {object}."

# print(make_sentence(object="Python", subject="Students", verb="learn"))

# # [------------------------------------------------------------------]

# # Q-24
# def apply_discount(price, discount=0):
#     return price - (price * discount / 100)

# print(apply_discount(1000))
# print(apply_discount(1000, 10))

# # [------------------------------------------------------------------]

# # Q-25
# def calculate_pay(hours, rate=200, bonus=0):
#     return hours * rate + bonus

# print(calculate_pay(40))
# print(calculate_pay(40, 250))
# print(calculate_pay(40, bonus=500))
# print(calculate_pay(hours=40, rate=300, bonus=1000))

# # [------------------------------------------------------------------]

# # Q-26
# def get_coordinates(x=0, y=0):
#     return x, y

# print(get_coordinates())
# print(get_coordinates(x=5))
# print(get_coordinates(y=10))

# # [------------------------------------------------------------------]

# # Q-27
# def compare(a, b):
#     if a > b:
#         status = "A is greater"
#         diff = a - b
#     elif b > a:
#         status = "B is greater"
#         diff = b - a
#     else:
#         status = "Equal"
#         diff = 0
#     return status, diff

# print(compare(15, 10))
# print(compare(5, 20))
# print(compare(7, 7))

# # [------------------------------------------------------------------]

# # Q-28
# def convert_temperature(value, scale="C"):
#     if scale == "C":
#         return (value * 9 / 5) + 32
#     elif scale == "F":
#         return (value - 32) * 5 / 9

# print(convert_temperature(0, "C"))
# print(convert_temperature(212, "F"))
# print(convert_temperature(100))

# # [------------------------------------------------------------------]

# # Q-29
# def calculate_result(marks, passing_marks=35):
#     return "Pass" if marks >= passing_marks else "Fail"

# print(calculate_result(45))
# print(calculate_result(30))
# print(calculate_result(45, passing_marks=50))

# # [------------------------------------------------------------------]

# # Q-30
# def order_summary(item, quantity=1, price=100, delivery_fee=40):
#     return (quantity * price) + delivery_fee

# print(order_summary("Book", delivery_fee=60))
# print(order_summary("Pen"))

# # [------------------------------------------------------------------]

# # Q-21
# def analyze_number(number):
#     abs_val = -number if number < 0 else number
#     is_even = number % 2 == 0
#     digit_count = len(str(abs_val))
#     return abs_val, is_even, digit_count

# print(analyze_number(-1234))
# print(analyze_number(560))

# # [------------------------------------------------------------------]

# # Q-22
# def calculate_stats(a, b, c):
#     smallest = min(a, b, c)
#     largest = max(a, b, c)
#     total = a + b + c
#     return smallest, largest, total

# print(calculate_stats(10, 5, 20))

# # [------------------------------------------------------------------]

# # Q-23
# def make_sentence(subject, verb, object):
#     return f"{subject} {verb} {object}."

# print(make_sentence(object="Python", subject="Students", verb="learn"))

# # [------------------------------------------------------------------]

# # Q-24
# def apply_discount(price, discount=0):
#     return price - (price * discount / 100)

# print(apply_discount(1000))
# print(apply_discount(1000, 10))

# # [------------------------------------------------------------------]

# # Q-25
# def calculate_pay(hours, rate=200, bonus=0):
#     return hours * rate + bonus

# print(calculate_pay(40))
# print(calculate_pay(40, 250))
# print(calculate_pay(40, bonus=500))
# print(calculate_pay(hours=40, rate=300, bonus=1000))

# # [------------------------------------------------------------------]

# # Q-26
# def get_coordinates(x=0, y=0):
#     return x, y

# print(get_coordinates())
# print(get_coordinates(x=5))
# print(get_coordinates(y=10))

# # [------------------------------------------------------------------]

# # Q-27
# def compare(a, b):
#     if a > b:
#         status = "A is greater"
#         diff = a - b
#     elif b > a:
#         status = "B is greater"
#         diff = b - a
#     else:
#         status = "Equal"
#         diff = 0
#     return status, diff

# print(compare(15, 10))
# print(compare(5, 20))
# print(compare(7, 7))

# # [------------------------------------------------------------------]

# # Q-28
# def convert_temperature(value, scale="C"):
#     if scale == "C":
#         return (value * 9 / 5) + 32
#     elif scale == "F":
#         return (value - 32) * 5 / 9

# print(convert_temperature(0, "C"))
# print(convert_temperature(212, "F"))
# print(convert_temperature(100))

# # [------------------------------------------------------------------]

# # Q-29
# def calculate_result(marks, passing_marks=35):
#     return "Pass" if marks >= passing_marks else "Fail"

# print(calculate_result(45))
# print(calculate_result(30))
# print(calculate_result(45, passing_marks=50))

# # [------------------------------------------------------------------]

# # Q-30
# def order_summary(item, quantity=1, price=100, delivery_fee=40):
#     return (quantity * price) + delivery_fee

# print(order_summary("Book", delivery_fee=60))
# print(order_summary("Pen"))



     