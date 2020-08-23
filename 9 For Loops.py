"""
we use for loop we just have to say

for (what we want to print) in (our list or dictonary)

when we have number and item we should have to pass both value as give below

There Are some break , continue , range statment which you understand in register because i write
there


"""

list=[
    ["RA",2],
    ["Jutt",66],
    ["shaka",12],
    ["bhoom",6]]

for item in list: # it will print[] in this form
    print(item)

for item , number in list: # it wil print in simple form
    print(item , number)

# A calculator which tells first it have to print only number and it only print number which are>6

for item , number in list:
    if number > 6:
        print(number) # it will print the number which are > 6 in our list

list1=[23,4332,2342,12,1121,23123,23,3,43,2,3,1,4,] # Best way of doing it
for item in list1:
    if str(item).isnumeric() and item > 6:
        print(item)
