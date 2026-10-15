nums = list(map(int, input("enter:-").split()))
for num in nums:
    if num < 0:
        break
    print(num, end=" ")