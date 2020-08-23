"""
What is global and Local Varaible
Gloabal Varaible which is used by every variable in
the program and
Local Variable which is used in only its function just like
in function1() we have both value of r but in function we are
using only local variable if we are outside the funtion and then
we print the value of the r then it use the gloabal variable
"""
r=60#Global Varible
def function1():
    r=50#Local variable
    print("Local Variable=",r)
function1()
print(r)

"""
so what if we want to use the global variable in a function or 
want to change the value of global variable in function so we use
the key word of global and then the variable name so it will 
change the global variable as in function()2
"""
def function2():
    global r
    r=300
    print("Gloabal Variable is",r)
function2()
