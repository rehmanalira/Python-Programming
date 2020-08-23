"""
Public which can use everyone
Protected which can use only selected classe
private which use the only one class

"""


class Student:
    name1=" Public name ->JUTT SB"
    _name2="protected name -->harry poter" # this is protected we write the protected variable by writing _(name)
    __name3="Private name" # by __ we write private name

Ali=Student()
print(Ali.name1) # it will print public name
print(Ali._name2) # it will print the proteced name

print(Ali._Student__name3) #it will print the private student name until we write first it class name