"""
A Program in which we have a hide number by which user has to find the number
we haveing a hiding number n=30
and it also have 5 chances when it gooes more than 5 it give message you lose if user guess the number message
it will say congrulation
"""

n=30
chance=1 #count starts from 1
chance2=4 # it give remaing chances
print("Note You have Only 5 chance")
while(chance<=5):#telling it has only 5 chance
    print("Enter Your Number")
    num = int(input())
    if(num==n):
        print("You Win Congrulation")
        break
    elif(num > 41):
        print("Number is greater")
    elif(num < 15):
        print("Number is lesser")
    elif(num ==25 or num>=15 or num<=40 or num==29 ):
        print("You are Nearby")



    print("remaing chance is",chance2)
    if(chance2==0):
        print("You Lose")
    chance=chance+1
    chance2=chance2-1
