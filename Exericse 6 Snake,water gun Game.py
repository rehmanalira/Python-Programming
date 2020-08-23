"""
It is snake water game means if other say snake and you say water
then snake will drink the water and you lose if you he say snake and
you say gun then you will win because gun kills the snake

so here we create a game  in which computer random take number and
you enter the number up to 10 time and who wins it tells at the end
most important is that we use c and y variable which tells the score
at the time when we print something so that is a good thing
"""

import random
list=["snake", "water", "gun"]#computer random list
i = 1
c=1#variable to calculate the number of wins for computer
y=1#variable to calculate the number of wins of You
while(i<=10):
    print("\nEnter Your Choice",i)
    print("s for snake")
    print("w for water")
    print("g for gun")
    num1 = input()
    game_list = random.choice(list)#here we get the random names
    if (game_list == "snake" and num1 == "w"):
        print("Computer Wins\n")
        c=c+1#here it counts
    elif (game_list == "water" and num1 == "w"):
        print("NO Win\n")
    elif (game_list == "gun" and num1 == "w"):
        print("You win\n")
        y=y+1#here it counts for you
    elif (game_list == "snake" and num1 == "s"):
        print("No win\n")
    elif (game_list == "water" and num1 == "s"):
        print("You wins\n")
        y=y+1
    elif (game_list == "gun" and num1 == "s"):
        print("Computer Wins\n")
        c=c+1
    elif (game_list == "snake" and num1 == "g"):
        print("You Win\n")
        y=y+1
    elif (game_list == "water" and num1 == "g"):
        print("Computer Wins\n")
        c=c+1
    elif (game_list == "gun" and num1 == "g"):
        print("No Win\n")
    else:
        print("Game End")

    print("Computer Choice was "+game_list+"\n")

    print("Your Score is", y)
    print("Computer Score is", c)
    i = i + 1

if(y>c):
    print("Congrulation You Wins :)")
elif(y==c):
    print("Match is Tie")
else:
    print("Sorry Computer Wins :(")


