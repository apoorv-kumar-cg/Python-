# Problem 2

marks = input("Enter marks separated by spaces: ").split()

fail = 0
passs = 0
good = 0
excellent = 0

for i in marks:
    s = int(i)
    if s < 35:
        fail += 1
    elif s <= 49:
        passs += 1
    elif s <= 74:
        good += 1
    else:
        excellent += 1

print(f"Fail student:- {fail}")
print(f"Pass student:- {passs}")
print(f"Good student:- {good}")
print(f"Excellent student:- {excellent}")