"""
Dunder methods:
which startes from "__" means __init__() is a dunder
method

there are two methods str and repr it will be print when we print the class but when we  print
the any class firt it will print the str if there is no str then it will print the repr method


"""

class Student:
    def __init__(self,sname,sclass,sage):
        self.name=sname
        self.section=sclass
        self.age=sage
    def show(self):
        print("Hello This is a show function")
    def __add__(self, other):
        return self.age + other.age # mapping Operator to a functon
    def __matmul__(self, other):# matrix multiplliction
        return self.age + other.age
    def __pow__(self, power, modulo=None): # taking power of a operator
        return self.age ** power.age
    def __repr__(self):
         return  f"jutt({self.name},  {self.age} ,{self.section})"

    def  __str__(self): # there are two methods str and repr it will be print when we print the class
        return f"The name is {self.name}"
ali=Student("Ali", "B",19)
jutt=Student("jutt", "A",20)
print(ali + jutt)
print(ali @ jutt)
print(ali ** jutt)
print(jutt)