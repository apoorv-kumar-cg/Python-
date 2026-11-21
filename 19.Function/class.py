# syntax

# def function_name()
#     function body
# fubction_name

# def student_record():
#     print("Name:-shayam")
#     print("Mark:-50")
#     print("-------------")

# student_record()
# student_record()
# student_record()

#[------------------------------------------------------------]

# a=10
# b=0

# def add():
#     print(a+b)
# def sub():
#     print(a-b)
# def mul():
#     print(a*b)  
# def div():
#     if b!=0:
#      print(a/b)
#     else:
#      print("b is zero")

# add()
# sub()
# mul()
# div()
#[------------------------------------------------------------]
# num=int(input("Enter number:-"))
# def even_odd():
#     if num%2==0:
#         print("Even")
#     else:
#         print("Odd")

# even_odd()
    
#[------------------------------------------------------------]
# def  add (a,b):
#     print(a+b)

# add(12,12)

#[------------------------------------------------------------]

# a = 10
# b = 20
# c = 40
# def add(a, b):
#     c = a + b
#     return c

# def sub(a, b):
#     return a-b

# def mul(a, b):
#     return a*b

# result = mul(sub(add(a,b),c),a)
# print(result)

#[------------------------------------------------------------]

# [PASS AS AN ARGUMENT TO ANOTHER FUNCTION]


# def double(number):
#     return number * 2

# def add_five(number):
#     return number + 5

# result = add_five(double(10))
# print(result)

#[------------------------------------------------------------]

# DEEFAULT ARGUMENTS
# Guest is default arguments

# def greet (name="Guest"):
#     print("Hello",name)

# greet()
# greet("Apoorv")

#[------------------------------------------------------------]

# def find_factorial(n): 
#     if n < 0:
#         return "Factorial does not exist for negative numbers"
    
#     # The factorial of 0 and 1 is always 1
#     if n == 0 or n == 1:
#         return 1
        
#     result = 1
#     for i in range(1, n + 1):
#         result *= i  
#     return result

# # Call the function
# num = 1111
# print(f"The factorial of {num} is: {find_factorial(num)}")

#[------------------------------------------------------------]

# def des(name,age,city):
#     print(name,age,city)

# # des(name="Apoorv",21,city="gaya")

# des(name="Apoorv",age=21,city="gaya")

#[------------------------------------------------------------]

# def hi(count):
#     count+=1
#     if count==5:
#         return count 
#     else:
#         return hi(count)


# print(hi(1)) 

# [------------------------------------------------------------]

# def couner_fun(count):
#     count+=1
#     if count==20:
#         return count
#     else:
#         return couner_fun(count)

# print(couner_fun(1))

# [------------------------------------------------------------]


# def info (name,a):
#     # print(name,a)
#     return name,a
# print(info("aa",89))

# [------------------------------------------------------------]


# def info(a,b,c,*args):
#     print(a,b,c)
#     print(args)

# info(1,2,3,4,5,6,7,8,9,0)

# [------------------------------------------------------------]

# def d(a=0,b=12,/,*,c,d):
#     return c+d,a+b
# print(d(c=12,d=12))

# [------------------------------------------------------------]

# def a(*args,**Kwargs):
#     print(Kwargs,args)
#     print(x,z)
#     print(type(Kwargs))
#     print(type(args))

# # a(1,2,3,4,5,6,7,8)
# a(4,5,6,7,8,9,0,q=1,w=2,e=3,x=22,z=44)

# [------------------------------------------------------------]

# word="call of"

# word=word.split()
# print(word)

# for i in word:
#     if i == "duty":
#         print("FOUND")
    
# [------------------------------------------------------------]

# sky=97

# word=input("Enter word:- ").lower()
# wor=0

# while sky<=122:
#     for i in word:
#         if i==chr(97):
#             wor+=1
#             print(chr(97),wor)
#             sky+=1

# print(chr(97))

# [------------------------------------------------------------]

# a=0
# b=1

# for i in range(8):
#     c=a+b
#     print(c)
#     a=b`
#     b=c
    
# [------------------------------------------------------------]

# def add(a, b, c):
#     return a + b + c

# numbers = 10, 20, 30
# print(add(*numbers)) 

# [------------------------------------------------------------] 

# def area(l,b):
#     # """
#     # *This is area of rectangle.
#     # *Area=length*breadth
#     # """
#     return l*b

# print(area.__doc__)
# print(area(12,13))

# [------------------------------------------------------------] 

# total=100
# def scope():
#     # total=10
#     print(total)
#     total=10
# scope()
# print(total)

# [------------------------------------------------------------] 

# x = 10

# def demo():
#     # global x
#     x+=1
#     print(x)
#     x = 20

# demo()  

# [------------------------------------------------------------] 

# def sum(a,b):
#     return a-b
# print(sum(b=10,a=3))

# [------------------------------------------------------------]
# items = []

# def reset_items():
#     global items
#     items = []

# reset_items()

# [------------------------------------------------------------]

# word=input("Enter word:-").strip().lower()


# length=len(word)


# a=1
# output=""
# for i in range (1,length):
#     if word[i]==word[i-1]:
#         a+=1
#     else:
#         output+=word[i-1]+"="+str(a)
#         a=1
# output+=word[length-1]+"="+str(a)
# print(output)
        
# [------------------------------------------------------------]

word = input("Enter word:- ").strip().lower()
                                                             
if word:
    a = 1
    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            a += 1
        else:
            print(f"{word[i - 1]}={a}  ")
            a = 1

    print(f"{word[-1]}={a}")
    
# [------------------------------------------------------------]

