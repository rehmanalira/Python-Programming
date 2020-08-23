"""
Diamond shape problem it is a problem which means which class is where derived
measn if there are four classes and then the A is class and B and C are derived
from A and there is another class which is derived from B and C
then if we use a method which means which method is called in python it will
simply solve it and but in c++ it will  made embugity java not suppport multipla
inheritance
"""
class A:
    def show(self):
        print("Rehman ALi RA A")
class B(A):
    def show(self):
        print("Rehman ALi RA B")
class C(A):
    def show(self):
        print("Rehman ALi RA C")
class D(B , C):
    pass


a= A()
b= B()
c= C()
d= D()
d.show()  #it will  print because first we use B or B is inherited firs