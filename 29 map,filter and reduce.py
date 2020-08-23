"""l1=["33","4","2","22"]
l1=list(map(int,l1))
addl=l1[0]+30
print(addl)

it is simply used to first it converts it into the int and then it will add
"""


"""def sq(a):
    return a*a #here we used a function to pass in map

mul=list(map(sq,num))"""
num=[3,22,21321,21321,33]

mul=list(map(lambda a:a*a,num))
print(mul)

"""def sq(a):
    return a*a
def cub(a):
    a*a*a
func=[sq , cub]

for i in range(19):

    mul1=list(map(lambda x:x(i),func))
    print(mul1)"""

#--------------filter---------

#it will check and return the greater or what we said to it means it retuurn true
num1=[3238,232,12,1,1213,243,2,23,21,3213,12,33]
def greater_20(num):
    return num>20
val=list(filter(greater_20,num1))
print(val)


#--------------reduce----

#first we impot it and it will do that it will multiply or add or what you want it do this to next item
#as here we multiply it to the next item here
from functools import reduce
num2=[1,4,3,2,4,3]

val2=reduce(lambda x,y:x*y,num2)
print(val2)