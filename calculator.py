
print("""enter [1] for ADD,
enter [2] for Sub,
enter [3] for Multiply,
enter [4] for Divide,
enter [5] for Floor Divide:-""")
c=int(input("enter:="))


if c==1 or c==2 or c==3 or c==4 or c==5:

  a=int(input("Enter first number:="))
  b=int(input("Enter second Number:="))
 

  if c==1:
    print(a+b)
  elif c==2:
    print(a-b)
  elif c==3:
    print(a*b)
  elif c==4:
    print(a/b)
  elif c==5:
    print(a//b)
else:
   print("Invalid enter")    