"""
A faulty calculator which takes input but give wrong
arithmetic operations :)
dont use as calculator :))))
"""

print("Enter first Number")
num1=int(input())
print("Enter your Operator")
num3=str(input())
print("Enter Second Number")
num2=int(input())
if num3=="+":
    print("Addtio  is",num1+num2-num1)
elif num3=="*":
    print("Multiplication is",num1+num2*num1)
elif num3=="-":
    print("Subtraction is",num1*num2+num1)
else:
    print("Division is",num1*num2-num1)