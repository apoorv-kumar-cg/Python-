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

# num=int(input("Enter number:="))
# choice=0

# for i in range(2,num):
#     if num%i==0:
#         choice+=1

# if choice==0:
#     print("Number is prime")
# else:
#     print("Number is not prime")

# [-------------------------------------------------------------------------------]

# num=int(input("""Enter number
#                   b/w 1 to 7:="""))

# match num:
#     case 1|2|3|4|5:
#          print("Weekday")
#     case 6|7:
#          print("Weekend")
#     case _:
#           print("Invalid choice")

# [-------------------------------------------------------------------------------]

# mark=int(input("Enter number:="))

# match mark:
#      case mark if mark>=90:
#           print("A")
#      case mark if mark>=70:
#           print("B")
#      case mark if mark>=60:
#          print("C")
#      case mark if mark>=50:
#                print("D")
#      case _:
#             print("FAIL")

# [-------------------------------------------------------------------------------]

# choice=int(input("""ENTER your choice:
#                         1 for call:-
#                         2 for talk:-
#                         3 for speak:-
#                         4 for end:- """))

# match choice:
#       case 1:
#          Enter=int(input("""Enter your choice:
#                               1 for call company Alpha:-
#                               2 for call company Bita:-
#                               3 for call company Gamma:-"""))
#          match Enter:
#             case 1:
#                print("Calling Alpha")
#             case 2:
#                print("calling bita")
#             case 3:
#                print("calling Gamma")
#       case 2:
#          Enter=int(input("""Enter your choice:
#                               1 for talk company Alpha:-
#                               2 for talk company Bita:-
#                               3 for talk company Gamma:-"""))
#          match Enter:
#             case 1:
#                print("talk Alpha")
#             case 2:
#                print("talk bita")
#             case 3:
#                print("talk Gamma")
#       case 3 :
#          Enter=int(input("""Enter your choice:
#                               1 for speak company Alpha:-
#                               2 for speak company Bita:-
#                               3 for speak company Gamma:-"""))
#          match Enter:
#             case 1:
#                print("Alpha speaking")
#             case 2:
#                print("bita speaking")
#             case 3:
#                print("Gamma speaking")

#       case 4:
#           print("CAll end")
#       case _:
#         print("Invalid input")

# [-------------------------------------------------------------------------------]

