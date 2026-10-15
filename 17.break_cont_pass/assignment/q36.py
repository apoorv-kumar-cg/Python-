nums =int(input("Enter:-").split())
target = int(input())
for n in nums:
    if n < 0:
        continue
    if n == target:
        print("Target found")
        break
else:
    print("Target not found")