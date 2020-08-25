"""
if we create a program which takes 3 minutes or some time to
run then what happen if user put wrong num and it also take
3 minutes to run and after 3 minutes it gives error
so avoiding this we use raise which means if input was wrong
it will not take time it just gave error

"""

name=input("ENter the number you ")
if name.isnumeric():
    raise ZeroDivisionError("You entered the an integer")
else:
    print(f"You name is {name}")