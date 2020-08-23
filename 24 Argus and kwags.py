"""
Args:
they are used to giving arugment to function and its class type
is tuple for more see on register
Kwargs
they are used giving arguments when we store a value in th
dictionary

"""



def fun1(*args):# we write args defining it by *name
    print("your name are ")
    for i in args:
        print(i)



li=["REhman ","Ali","RA","JUTT","hundey"]
fun1(*li)

def fun2(**kwargs):
    print("You List is")
    for key,value in kwargs.items():
        print(key,value)
#key is first and value is after:eg->kha hu

kw={"Helo":"kha ha","You":"ider he hu yr"}
fun2(**kw)