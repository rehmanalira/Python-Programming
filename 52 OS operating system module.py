"""
Os is operating system which order to do  something like that eg rename of file or remove of any
file or want to knoe the directory of the file etc.

"""

import os
print(os.getcwd()) # this will get current directory
#print(os.mkdir("Jutt")) # this will make a directory
#print(os.makedirs("R/A")) # this will make a directory and another directory in the in the directory
 #print(os.rename("shaka.txt","RA.txt")) # it will re name

print(os.path.exists("R:/songs")) # it tells that if this path exsisits are not
print(os.path.isfile("RA.txt")) # it will tells that is this file exsists in it or not
print(os.listdir("R://")) # it will give all list
print(os.chdir()) # it will change the directory