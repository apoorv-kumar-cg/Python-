nums = int(input("Enter:-").split())
target = int(input())
for num in nums:
    if num == target:
        print("Found")
        break
else:
    print("Not found")