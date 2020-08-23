""""
So IT IS A PROGRAM WHICH REMIND YOU TO DRINK WATER AND TAKE EXERCISE AFTER FEW MINUTES
THIS WILL HELP YOU TO REMINDING YOU

ALSO FIRST RUN THE PROGRAM :)
"""


from datetime import datetime#here importing the date and time which tells us date and time
from time import time#here importing time from time we can also write time.time()
from pygame import mixer#mixer is a py game module which is used to run a mp3 or any audio to your python program
mixer.init()#it is used to initialze the mixer it is importan to loading music file in mixer
#-------------function of drinking water----
def drink_water():
    mixer.music.load("water.wav")   #here we load the music file and between "" we gave the music file we can also give path here
    mixer.music.play(-1)    #here we play the music file and i write -1 because it will run the music file again and again
    print("Enter q if you drink water and e to exit the whole program")
    button = input()
    while True:     #if we cant use while then our music file not haveing time to run the file so it is important if we loading a file
        if (button == "q"):
            mixer.music.stop()
            break
        elif button=="e": #it will exit the program if we press e
            exit()
        else:
            print("you entered wrong KeyI am exiting the Program") #here if we press any wrong key it will exit the program
            exit()
#---------------Eyes set functionn-------
def eyes_rest(): #it works also similarly as above works
    mixer.music.load("eyes.wav")
    mixer.music.play(-1)
    print("Enter q if you wash your eyes e to exit the whole program")
    button = input()
    while True:
        if(button=="q"):
            mixer.music.stop()
            break
        elif button=="e":
            exit()
        else:
            print("you entered wrong key I am Exiting the Program")
            exit()
#---------------Exercise Function-----------
def exer_cise(): #Same function As Above
    mixer.music.load("exercise.wav")
    mixer.music.play(-1)
    print("Enter q if you take the exercise e to exit the whole program")
    button=input()
    while True:
        if(button=="q"):
            mixer.music.stop()
            break
        elif button=="e":
            exit()
        else:
            print("you entered wrong key I am exiting Program")
            exit()


#------------REcording Our History--------
def health_history(str):    #here we take a string argument which take string and write it in file.write({str})
    #this function record our history when we drink and take exercise our wash our eyes
    with open("MY water,eyes and exercise teller.txt","a") as file: #opening file and set it to the append mode
        file.write(f"I {str} at time-> {datetime.now()}\n") #here we writing the file


"""
THIS initail_water=time this part is very IMORTANT TO understand
SO BASICALLY WHAT HAPPENING HERE HERE WE HAVE A FUNCTION WHIC IS KNOW AS time()
it gives the time in secons which have been coming from UNIX DATE 1 january 1970
if you write print(time()) then you get the seconds

HERE WE INITAILISE THIS TIME TO initail_water WHICH MEANS WHEN WE GO IN THE WHILE LOOP
WE HAVE WRITE 
if time() - initial_water > water           #where water value is = 
WHEN THIS CONDTION WILL BE TRUE THEN IT WILL RUN THE MEANS HERE NUMBER OF SECONDS BECOME GREATER THAN THE water
and it will run the PROGRAM simply if number of seconds become greater thane > giver value it will run the
Program

here i initalise them with time()


IN MOST SIMPLE WORDS IT IS CONDTION WHICH WILL REMIND US AFTER THE TIME WHICH WE GAVE AFTER THE > 

"""
initail_water=time()
initial_eyes=time()
initial_exer=time()

water= 30*60#it is time which will after it reminds here 30 is minutes and 60 is second
eyes=2*60*60 # time  which take  2 is hours
exer=3*60*60 #here it takes 3 hours

if __name__ == '__main__': #it is main funtion first it will be executed

    print("Enter 's' to start the program and when you want to exit the program just press 'e'")
    button=input()
    if button=="s":
        #we use while because it will run the program again and again
        #IT IS IMPORTANT TO USE ONLY if CONDTION AS I USE
        while True:
            if time() - initail_water > water:  #here i give condtions if number of seconds > water than it will run it
                drink_water()
                health_history("Drink Water")
                initail_water = time()
            if time() - initial_eyes > eyes:
                eyes_rest()
                health_history("take the rest of eyes")
                initial_eyes = time()
            if time() - initial_exer > exer:
                exer_cise()
                health_history("Do exercise ")
                initial_exer = time()
    elif button=="e":
        exit()

