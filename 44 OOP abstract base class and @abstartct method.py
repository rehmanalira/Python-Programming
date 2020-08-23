"""
so basically when we made a class and we want that a function
must be written the we use the ABC and abstarctmethod
and for this first we made base class and then in base class
we define the method which have to must be used

"""


from abc import ABC , abstractmethod # importing
class detail(ABC): # base class
    @abstractmethod
    def report(self): # defining the method that must be used
        return 0


class Student(detail):
    def __init__(self):
        self.name="Ali JUtt"
        self.age=19
        self.school="The concept college"
    def report(self): # here we define the method if we  not define this it will gave the error
        print("The repoprt of the shtudent is -->")
stdnt1=Student()
print(stdnt1.age)
