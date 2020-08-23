"""
Inheritance:
in this we inhert all the properity of one class into another class
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


    #-----------Satic--------
    @staticmethod # by thisb we define the static method
    def show(str):#our function
        print("This is " + str)

class Student(Employe):#made another class and inherit by (class name which we wantto inherit)
    def __init__(self,rname,rage,rstudy,rsection):# made an constructor for adding more info in the class
        self.name = rname
        self.age = rage
        self.study = rstudy
        self.section=rsection

    def show1(self):# A function for getting the values

        return f"The name is{self.name} and the age is {self.age} and The sectin is{self.section} "


jutt=Student("Jutt" ,"18" ,"Nothing" ,"A")
print(jutt.show1())#printing the jutt object



