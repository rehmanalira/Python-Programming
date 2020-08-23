"""
Basically in python we know functions are built in mean they are defined
but what if we want to make our own fucntion so lets see
"""

def function1(a,b): #we define function by writing def and function name

    average=(a+b)/2
    print("Average is",average)
    return average
#print(function1(23,33)) # we can also print like this but when we have no return value it will give none

function1(44,22) #this is function we can call it how much we want

v=function1(555,44333)
print(v) # here we stored the function in the variable

#Doc Sring

def sum(num1,num2):
    """ This is Doc String means first line of function which is commented is called doc string this help us to know  about the function"""
    sum=num1+num2
    return sum
print(sum(22,33))
print(sum.__doc__) #this is how we can know about doc string