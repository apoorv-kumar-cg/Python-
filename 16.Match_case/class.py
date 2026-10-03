# a=int(input("Enter 1st number:="))
# b=int(input("Enter 2st number:="))
 
# choice=int(input("Enter no 1 for add,2 for sub,3 for multiply,4 for divide:="))

# match choice:
#     case 1:
#         print(a+b)
#     case 2:
#         print(a-b)
#     case 3:
#         print(a*b)
#     case 4:
#         print(a/b)
#     case _:
#         print("Invalid choice")

# [-------------------------------------------------------------------------------]

# a=int(input("Enter 1st number:="))
# b=int(input("Enter 2st number:="))

# choice=int(input("""Enter number-
#                     1 for add:
#                     2 for sub:
#                     3 for multiply:
#                     4 for divide: 
#                     AND enter 0 for stop:="""))
# while choice!=0:
    
#     match choice:
#             case 1:
#               print(a+b)
#             case 2:
#               print(a-b)
#             case 3:
#                print(a*b)
#             case 4:
#                 if b==0:
#                    print("Number 2 should not equal to zero")
#                 else:
#                    print(a/b)
#             case _:
#                 print("Invalid choice")

#     choice=int(input("""Enter number
#                         1 for add:
#                         2 for sub:
#                         3 for multiply:
#                         4 for divide: 
#                         AND enter 0 for stop:="""))
#     if choice==0:
#         print("Loop stop")
#     else:
#         a=int(input("Enter 1st number:="))
#         b=int(input("Enter 2st number:="))

# [-------------------------------------------------------------------------------]
        

n=int(input("Enter:="))
for i in range(2,n+1):
    print(i)
    if n%i!=0:
      print("Prime")


if n==2:
   print("prime number")
if n==1:
   print("NON PRIME NON COMPOSIT")


