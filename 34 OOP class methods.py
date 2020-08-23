"""
we using class method when we create a function in the class also take the value of
as self but we not want that it take sthe value as self
so we use class method also if we want the change the value of the gloabal value of the
class so we can similary change with the class methods

"""
class Employe:
    variable=50
    #This is constructor
    def __init__(self,rname,rage,rstudy):
        self.name=rname
        self.age=rage
        self.study=rstudy


    def show(self):#here self is an argument which take any of obejct which given and the the function name
        print(f"My name is {self.name} , My age is {self.age} and i am studying in{self.study}")

    @classmethod #using class method
    def new_variable(cls,new_v):#creat function and pass the new value which we want to change
         cls.variable=new_v

RA= Employe("Rehman Ali","19","GUCF")

RA.new_variable(99999999)
print(RA.variable)


