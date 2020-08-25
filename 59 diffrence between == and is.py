"""
COPied from web site


The == operator compares the values of both the operands and checks for value
equality. Whereas
is operator checks whether both the operands refer to the same object or not.



# python3 code to
# illustrate the
# difference between
# == and is operator
# [] is an empty list
list1 = []
list2 = []
list3=list1

if (list1 == list2):
    print("True")
else:
    print("False")

if (list1 is list2):
    print("True")
else:
    print("False")

if (list1 is list3):
    print("True")
else:
    print("False")

list3 = list3 + list2

if (list1 is list3):
    print("True")
else:
    print("False")
Output:

True
False
True
False

Output of the first if condition is “True” as both list1 and list2 are empty lists.

Second if condition shows “False” because two empty lists are at different
memory locations.
 Hence list1 and list2 refer to different objects. We can check it with id()
 function in python which returns the “identity” of an object.
Output of the third if condition is “True” as both list1 and list3 are
pointing to the same object.
Output of the fourth if condition is “False” because concatenation of
two list is always produce a new list.


"""