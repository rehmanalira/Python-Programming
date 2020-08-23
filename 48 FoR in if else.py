"""
It is used when we have to find something in our list

"""
list=["jutt", "butt", "rana"]
cast = str(input("Enter the cast"))
for i in list:
    if i == cast:
        print("We have this cast")
        break
else:
    print("we dont have this cast")
