"""
This is a program which named as HEalth system
It works as it in this you can enter your details
what you eat at the day and what you do exercise in the day
in this you can also check the what you entered


NOTE: here just one updation you have to write the time when a use enter that
so just have to write when you writing a file
fot this you have to this
food.write(str(getdate())+food)<------->

"""


# A function which tells the time write  now
def getdata():
    import datetime
    return datetime.datetime.now()

    # Checking Data Function


def checkingDetails():  # here is a function which is used to checking the entered details
    # previously by the user
    print("Press 1 for Checking Rehman Details")
    print("Press 2 for Checking Rizwan Details")
    print("Press 3 for Checking Tayyab details")
    c = int(input())  # it is a variable c to take an integer input
    if (c == 1):
        print("Rehman Health Details are Given")
        print("Press 1 for checking Food Details")
        print("Press 2 for Checking Exercise Details")
        d = int(input())  # it is also a variable to take integer input
        # Food checking details
        if (d == 1):  # it will read the data and it will print the data that user input previously
            print("Food Details are")
            with open("Rehman food.txt") as f3:
                contentent = f3.read()
                print(contentent)

                # Exercise Checking details
        elif (d == 2):
            print("Exercise Details are")
            with open("Rehman Exercise.txt") as f3:
                contentent = f3.read()
                print(contentent)  # it will check the exercise and it will print the exercise
        else:
            print("You Entered Wrong Number bRO")

            # Rizwan Checking Details
    elif (c == 2):
        print("Rizwan Health Details are Given")
        print("Press 1 for checking Food Details")
        print("Press 2 for Checking Exercise Details")
        d = int(input())
        # Food checking details
        if (d == 1):
            print("Food Details are")
            with open("Rizwan food.txt") as f3:
                contentent = f3.read()
                print(contentent)

                # Healt Checking details
        elif (d == 2):
            print("Exercise Details are")
            with open("Rizwan Exercise.txt") as f3:
                contentent = f3.read()
                print(contentent)
        else:
            print("You Entered Wrong Number bRO")

            # Tayyab Checking Details
    elif (c == 3):
        print("Tayyab Health Details are Given")
        print("Press 1 for checking Food Details")
        print("Press 2 for Checking Exercise Details")
        d = int(input())
        # Food checking details
        if (d == 1):
            print("Food Details are")
            with open("Tayyab food.txt") as f3:
                contentent = f3.read()
                print(contentent)

                # Healt Checking details
        elif (d == 2):
            print("Exercise Details are")
            with open("Tayyab Exercise.txt") as f3:
                contentent = f3.read()
                print(contentent)
        else:
            print("You Entered Wrong Number bRO")

    else:
        print("You Entered Wrong Number BRo")

        # Enerinng Data Function


def system():  # it is a function which is used to enter the data from the user
    print("Welcome To RA Health System")
    print("Press 1 for Rehman")
    print("Press 2 for Rizwan")
    print("Press 3 for Tayyab")
    a = int(input())  # it is a variable to store the integer

    # REHMAN SECTION--->
    if (a == 1):
        print("Rehman Health Detail")
        print("Press 1 for Entering Food Details")
        print("Press 2 for Entering Exercise Details")
        b = int(input())  # it is also variable

        # Food details

        if (b == 1):
            print("Please Enter Your Food Details")
            print("Write what you Eat all the day")
            with open("Rehman food.txt", "a") as f1:
                food = input()
                f1.write(str(getdata())+food)#here i gave the date and time
                print("You Entered Successfully", "(", food, ")")
                print("At the time of", getdata())

                # Exercise details

        elif (b == 2):
            print("Please Enter Your Exercise Details")
            print("Enter what You Exercise whole day")
            with open("Rehman Exercise.txt", "a") as f2:
                exercise = input()
                f2.write(exercise)
                print("You Entered Exercise Successfully", "(", exercise, ")")
                print("At the time of", getdata())

        else:
            print("You Entered Wrong Number")

            # RIZWAN SECTION--->
    elif (a == 2):
        print("Rizwan Health Details")
        print("Press 1 for Entering Food Details")
        print("Press 2 for Entering Exercise Details")
        b = int(input())

        # Food Details

        if (b == 1):
            print("Please Enter Your Food Details")
            print("Write what you Eat all the day")
            with open("Rizwan food.txt", "a") as f1:
                food = input()
                f1.write(food)
                print("You Entered Successfully", "(", food, ")")
                print("At the time of", getdata())
            # Exercise Detils

        elif (b == 2):
            print("Please Enter Your Exercise Details")
            print("Enter what You Exercise whole day")
            with open("Rizwan Exercise.txt", "a") as f2:
                exercise = input()
                f2.write(exercise)
                print("You Entered Exercise Successfully", "(", exercise, ")")
                print("At the time of", getdata())
        else:
            print("You Entered Wrong Number")

        # TAYYAB SECTION---->
    elif (a == 3):
        print("Tayyab Health Details")
        print("Press 1 for Entering Food Details")
        print("Press 2 for Entering Exercise Details")
        b = int(input())
        # Food Details

        if (b == 1):
            print("Please Enter Your Food Details")
            print("Write what you Eat all the day")
            with open("Tayyab food.txt", "a") as f1:
                food = input()
                f1.write(food)
                print("You Entered Successfully", "(", food, ")")
                print("At the time of", getdata())
            # Exercise Details

        elif (b == 2):
            print("Please Enter Your Exercise Details")
            print("Enter what You Exercise whole day")
            with open("Tayyab Exercise.txt", "a") as f2:
                exercise = input()
                f2.write(exercise)
                print("You Entered Exercise Successfully", "(", exercise, ")")
                print("At the time of", getdata())
        else:
            print("You Entered Wrong Number")
    else:
        print("You Input Wrong Number")


print("-----WELCOME to RA HEALTH SYSTEM-------")
print("Press 1 for Entering Your details")
print("Press 2 for Checking Entered Details")
entering = int(input())
if (entering == 1):
    system()
elif (entering == 2):
    checkingDetails()
else:
    print("--You Entered Wrong Number---")
