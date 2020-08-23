"""
Global and instance
global means in class the are define inside the class and every where we can use it but
global variable can be changed only by the classs

Instance variable
means every object ha its own variable and another object cannot access that variable

"""


class Student:
    village="209 GB"
    pass

RA=Student()
RT=Student()

RA.name="Rehman ALi RA" #these are instance variables
RA.age=19
RA.study="GCUF"

RT.name="Rehman TAyyab" #instance
RT.age=17
RT.study="Concept colleg"

print(RA.name, RA.age, RA.study)
print(RT.name, RT.age, RT.study)

print("global Variable")
print(RA.village, RT.village)
print("Here we changin global variable value")

Student.village="Faislabad"
print(Student.village, RA.village, RT.village)