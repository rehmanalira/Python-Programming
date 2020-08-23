"""def fun1(n): #this is itreative which is not running
    fact=1
    for i in range(n):

        fact = fact * (i+1)
        return fact
print(fun1(num))
        """

"""
Recursive functions are thoes in which we can call its function 
until the condtion become true or get its result
"""
def fun_recursive(n):
    if n==1 or n==0:
        return 1
    else:
        return n * fun_recursive(n-1)#here we call its funcction and multiply it with the number


print("Enter You Number")
num=int(input())
print(fun_recursive(num))