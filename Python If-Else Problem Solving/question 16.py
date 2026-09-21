unit=int(input("Enter electricity units="))

if unit<=100:
    print(f"Bill is {unit*5}")

elif unit<=200:
    first_hunderd=100*5
    second_hunderd=(unit-100)*7
    print(f"Bill is {first_hunderd+second_hunderd}")
          
else:
     first_hunderd=100*5
     second_hunderd=(first_hunderd-unit)*7
     other_unit=(unit-200)*10
     print(first_hunderd+second_hunderd+other_unit)
