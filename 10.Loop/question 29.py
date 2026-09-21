# for row in range(5):
#     bag=""
#     for colomn in range (row):
#         for i in range (1,row+1):
#             print(i,end="")
#     print()

for i in range(5):
    bag=''
    for j in range(i+1):
        bag+=str(j+1)
    print(bag)