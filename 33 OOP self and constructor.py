"""
if we create a function inside the class it takes an argument whicch is self means when we write any
name and after that we use the .name then self will be taken as the argument which you made
for example
RA.name
here RA will be go as an argument
Constructor is just like also self here we can give name and addres and what we want as an argument
but we have to write __init__ to define the constructor and after that we will gave the arguments

"""


class Employe:
    #This is constructor
    def __init__(self,rname,rage,rstudy):
        self.name=rname
        self.age=rage
        self.study=rstudy


    def show(self):#here self is an argument which take any of obejct which given and the the function name
        print(f"My name is {self.name} , My age is {self.age} and i am studying in{self.study}")


RA= Employe("Rehman Ali","19","GUCF")

""" RA.name = "Rehman Ali"  # instance
RA.age = 17
RA.study = "GCUF"

s= Employe()
s.name = "Sajjad Ali"  # instance
s.age = 39
s.study = "UNI"
print(RA.show()) """
print(RA.name)
print(RA.study)