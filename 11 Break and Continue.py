"""

break and continue we already discus
"""
i=0
while(True):#true means it will run again and again with no stop

    if(i<5):
        i=i+1
        continue # it will not run that until contion is true

    print(i,end=" ")
    if(i==11):

        break
    i=i+1


    """ 
    QUIZ 
    A program whic takes all number except 100 or greater than 100
    """

while(True):
    print("Enter Number:")
    num=int(input())
    if(num==100 or num>100):
        print("You Entered Number above then 100")

        break

    num=num+1








