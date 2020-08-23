"""
TRY, EXCEPT, FINALLY ,ELSE

as we know try are used when a program give error but we want print the next statment and also it will print the
error but it will also print the next statment the error will be not in the red lines

FINALLY:
we use it when we have to importantly print this means a program do all stuff but it will must do the stuff
which is in finally statment

Else
it will run when except will not run

"""

f=open("RA.txt")
try:
    file=open("shaka.txt")
except Exception as e:
    print(e)

else: # if created a file which is present in except the except condtion will become false and else condtion
    # be tru then else will be run
    print("It will run when except will not run or when except is not true")
finally: # it is used when we have to do this thing importantly means this will happen in program
    f.close()
    try:
           file.close() # this will give error   so we use it here as try and except
    except Exception as i:
        print(i)
print("This is End oF every ting means it will run ")





