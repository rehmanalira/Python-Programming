"""
why we using Class alternative see the register

"""

class Employe:
    variable=50
    #This is constructor
    def __init__(self,rname,rage,rstudy):
        self.name=rname
        self.age=rage
        self.study=rstudy



    @classmethod #using class method
    def new_variable(cls,new_v):#creat function and pass the new value which we want to change
         cls.variable=new_v
    @classmethod
    def from_dash(cls,string):#give an argument which take string

        return cls(*string.split("-")) #here we split that we want


RA= Employe("Rehman Ali","19","GUCF")

shaka=Employe.from_dash("shaka-20-shaklaka")#here is function whic we cant want to write above function

"""RA.new_variable(47438383)
print(RA.variable)"""

print(shaka.age)
