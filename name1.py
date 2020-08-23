"""
so here we create a normal function which shows and multiply
so what if we want access these functions to other file we just made
a file import this file name just as in file name2

basically when we acces name1 in name it will executed all instructions of name1 also so we us "main"
which means after this the next part will not be executed
"""

def show(string):
    return f"This is RA and you are{string}"
def mult(num1,num2):
    return num1*num2

if __name__ == '__main__':#after this part will not be executed and all previous function will be use able

    print(show("Your Friend meri jan"))
    print(mult(50,10))