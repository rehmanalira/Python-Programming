"""
there are module in python which means they are already written
there is no need to write them
for example if we have to find a random nunmber then there ie no
need to write a random number function we just have to use this
already written function in python to use this we write
import module name<--->

if there is no module in this you can download it by writting
pip install (module name )
"""
import random#it is imporatant to use built in moudule
r1=random.randint(1,30)#it  will use the random number from 1 to 30
print(r1)
r2=random.random() *10#when we multiply it by number it give random number to that number
print(r2)

list=["Rehman","Ahsan","Jani","Tayyab"]
r3=random.choice(list)#it will  give the random list name by writting choice
print(r3)