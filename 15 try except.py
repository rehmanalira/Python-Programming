"""
try and except are two keywords which are used when our program is run and give error but we want get error and want to
print the next statment

"""
try: #which  will run this if it throw erroe then it will give only error message but it will not exit the program
    print("Enter the number")
    num1=int(input())
    print("Enter Second Number")
    num2=int(input())
    sum= num1+num2
    print(sum) #if we put the value which is integer and then the value of string it will throw error

except Exception as e:
                   print(e)

print("MA Print hu gya ") # if we use try and except and then it will not throw error it gives location of error and also print this value