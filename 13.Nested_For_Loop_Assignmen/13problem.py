# # Problem 13


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j*2-1,end=" ")
#     print()


# for i in range(6):
#     a=1
#     for j in range(i):
#         print(a,end=" ")
#         a+=2
#     print()


for i in range(6):
    a=0
    for j in range(10):
        a+=1
        print(a)
        for row in range(5):
           for col in range(row):
               if a%2!=0:
                    print(a,end=" ")
               else:
                   print()
            





